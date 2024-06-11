# import os.path
#
# import pytest
# from api import PetFriends
# from settings import valid_email, valid_password
#
# class TestPetFriends:
#     @pytest.fixture(autouse=True)
#     def setup(self):
#         self.pf = PetFriends()
#
#     def test_get_api_key_for_valid_user(self, email=valid_email, password=valid_password):
#         status, result = self.pf.get_api_key(email, password)
#         assert status == 200
#         assert 'key' in result
#
#     def test_get_all_pets_with_valid_key(self, filter=''):
#         _, auth_key = self.pf.get_api_key(valid_email, valid_password)
#         status, result = self.pf.get_list_of_pets(auth_key, filter)
#         assert status == 200
#         assert len(result['pets']) > 0
#
#     def test_add_new_pet_whithout_photo(self, name ='Стасик', animal_type= 'Таракан', age = '3'):
#         _, auth_key = self.pf.get_api_key(valid_email, valid_password)
#         status, result = self.pf.add_new_pet_whithout_photo(auth_key, name, animal_type, age)
#         assert status == 200
#         assert result['name'] == name
#
#     def test_add_new_pet_with_valid_data(self, name='Тузя', animal_type='кошка', age='3', pet_photo='images/cat.jpg'):
#         pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
#         _, auth_key = self.pf.get_api_key(valid_email, valid_password)
#         status, result = self.pf.add_new_pet(auth_key, name, animal_type, str(age), pet_photo)
#         assert status == 200
#         assert result['name'] == name
#
#     def test_update_pet_info(self, name='Гадя', animal_type='Кот', age=15):
#         _, auth_key = self.pf.get_api_key(valid_email, valid_password)
#         _, myPets = self.pf.get_list_of_pets(auth_key, "my_pets")
#
#         if len(myPets['pets']) > 0:
#             status, result = self.pf.update_pet_info(auth_key, myPets['pets'][0]['id'], name, animal_type, age)
#             assert status == 200
#             assert result['name'] == name
#         else:
#             raise Exception("There is no my pets")
#
#     def test_delete_pet(self,):
#         _, auth_key = self.pf.get_api_key(valid_email, valid_password)
#         _, myPets = self.pf.get_list_of_pets(auth_key, 'my_pets')
#
#         if len(myPets['pets']) == 0:
#             self.pf.add_new_pet(auth_key, 'Тузя'  'кошка', "3", "images/cat1.jpg")
#             _, myPets = self.pf.get_list_of_pets(auth_key, "my_pets")
#
#         pet_id = myPets['pets'][0]['id']
#         status, _ = self.pf.delete_pet(auth_key, pet_id)
#         _, myPets = self.pf.get_list_of_pets(auth_key, "my_pets")
#
#         assert status == 200
#         assert pet_id not in myPets.values()
#
import os
import pytest
from api import PetFriends
from settings import valid_email, valid_password

class TestPetFriends:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.pf = PetFriends()

    def test_get_api_key_for_valid_user(self, email=valid_email, password=valid_password):
        status, result = self.pf.get_api_key(email, password)
        assert status == 200
        assert 'key' in result

    def test_get_all_pets_with_valid_key(self, filter=''):
        _, auth_key = self.pf.get_api_key(valid_email, valid_password)
        status, result = self.pf.get_list_of_pets(auth_key, filter)
        assert status == 200
        assert len(result['pets']) > 0

    def test_add_new_pet_whithout_photo(self, name='Михаил', animal_type="Скунс", age='3'):
        _, auth_key = self.pf.get_api_key(valid_email, valid_password)
        status, result = self.pf.add_new_pet_whithout_photo(auth_key, name, animal_type, age)
        assert status == 200
        assert result['name'] == name

    def test_add_new_pet_with_valid_data(self, name='Тузик', animal_type='Кот', age='3', pet_photo='images/cat.jpg'):
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
        _, auth_key = self.pf.get_api_key(valid_email, valid_password)
        status, result = self.pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
        assert status == 200
        assert result['name'] == name

    def test_add_new_pet_with_valid_data_2(self, name='Чав', animal_type='Хомяк', age='4', pet_photo='images/pomchi-mixed-dog-bre.jpg'):
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
        _, auth_key = self.pf.get_api_key(valid_email, valid_password)
        status, result = self.pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
        assert status == 200
        assert result['name'] == name

    def test_update_pet_info(self, name='Мурзик', animal_type='Кот', age=15):
        _, auth_key = self.pf.get_api_key(valid_email, valid_password)
        _, my_pets = self.pf.get_list_of_pets(auth_key, "my_pets")

        if len(my_pets['pets']) > 0:
            status, result = self.pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
            assert status == 200
            assert result['name'] == name
        else:
            pytest.fail("There is no my pets")

    def test_delete_pet(self):
        _, auth_key = self.pf.get_api_key(valid_email, valid_password)
        _, my_pets = self.pf.get_list_of_pets(auth_key, 'my_pets')

        if len(my_pets['pets']) == 0:
            pytest.fail("There is no my pets to delete")

        pet_id = my_pets['pets'][0]['id']
        status, _ = self.pf.delete_pet(auth_key, pet_id)
        _, my_pets_after_deletion = self.pf.get_list_of_pets(auth_key, "my_pets")

        assert status == 200
        assert all(pet['id'] != pet_id for pet in my_pets_after_deletion['pets'])

    def test_delete_pet_2(self):
        #  удалялем последнего в списке
        _, auth_key = self.pf.get_api_key(valid_email, valid_password)
        _, my_pets = self.pf.get_list_of_pets(auth_key, 'my_pets')

        if len(my_pets['pets']) == 0:
            pytest.fail("There is no my pets to delete")

        pet_id = my_pets['pets'][-1]['id']
        status, _ = self.pf.delete_pet(auth_key, pet_id)
        _, my_pets_after_deletion = self.pf.get_list_of_pets(auth_key, "my_pets")

        assert status == 200
        assert all(pet['id'] != pet_id for pet in my_pets_after_deletion['pets'])

    # Негативные тест-кейсы

    def test_get_api_key_for_unvalid_user(self, email="", password=valid_password):
        status, result = self.pf.get_api_key(email, password)
        assert status == 403 or status == 401
        print(status)

    def test_get_api_key_for_unvalid_password(self, email=valid_email, password=''):
        status, result = self.pf.get_api_key(email, password)
        assert status == 403 or status == 401
        print(status)

    def test_add_new_pet_with_invalid_data(self, name='Тузя', animal_type='кошка', age='3', pet_photo=''):
        # Попытка добавления нового питомца с пустым путем к фотографии
        try:
            _, auth_key = self.pf.get_api_key(valid_email, valid_password)
            status, result = self.pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
            print(f"Status code: {status}")
            print("Result:", result)
            assert status != 200, f"Expected status code not to be 200, got {status}"
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_add_new_pet_whithout_photo_with_negative_age(self, name='Палкан', animal_type='Барбос', age='-3'):
        _, auth_key = self.pf.get_api_key(valid_email, valid_password)
        status, result = self.pf.add_new_pet_whithout_photo(auth_key, name, animal_type, age)
        # Проверяем, что статус ответа равен 400
        assert status == 400, f"Unexpected status code: {status}"
        # Если статус код 200, но возраст питомца отрицательный, что является некорректным, печатаем ошибку
        if status == 200 and int(age) < 0:
            print(f"Error: Pet was created with negative age. Status code: {status}, Response: {result}")

    def test_add_new_pet_whithout_photo_with_empty_field(self, name='Палкан', animal_type='', age='7'):
        _, auth_key = self.pf.get_api_key(valid_email, valid_password)
        status, result = self.pf.add_new_pet_whithout_photo(auth_key, name, animal_type, age)
        # Проверяем, что статус ответа равен 400
        assert status == 400, f"Unexpected status code: {status}"
        # Если статус код 200, но возраст питомца отрицательный, что является некорректным, печатаем ошибку
        if status == 200 and int(age) < 0:
            print(f"Error: Pet was created with negative age. Status code: {status}, Response: {result}")

    def test_update_pet_info_with_long_name(self, name='N' * 1000, animal_type='Кот', age=15):
        _, auth_key = self.pf.get_api_key(valid_email, valid_password)
        _, my_pets = self.pf.get_list_of_pets(auth_key, "my_pets")

        if not my_pets['pets']:
            pytest.fail("There is no my pets")

        pet_id = my_pets['pets'][0]['id']
        status, result = self.pf.update_pet_info(auth_key, pet_id, name, animal_type, age)

        # Проверяем, что статус код равен 400 из-за слишком длинного имени
        assert status == 400, f"Expected status code 400 for long name, got {status}"

        # Если статус код 200, что является некорректным, выводим сообщение об ошибке
        if status == 200:
            print(f"Error: Pet info was updated with too long name! Status code: {status}, Response: {result}")

    def test_update_pet_info_with_nonexistent_pet_id(self, name='Татошка', animal_type='Лягушка', age=57):
        _, auth_key = self.pf.get_api_key(valid_email, valid_password)

        # Генерируем несуществующий ID питомца
        nonexistent_pet_id = 'nonexistent_id'

        # Пытаемся обновить информацию о питомце с несуществующим ID
        status, result = self.pf.update_pet_info(auth_key, nonexistent_pet_id, name, animal_type, age)

        # Проверяем, что статус код равен 404
        assert status == 404, f"Expected status code 404 for nonexistent pet id, got {status}"

        # Проверяем, что в ответе нет информации о питомце
        assert 'name' not in result or result['name'] != name, "Pet info should not be present for nonexistent pet id"

