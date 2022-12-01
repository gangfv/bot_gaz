from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

from markups import *
from setting import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    username = message.from_user.first_name
    await message.answer(
        f"Добро пожаловать, {username}\n"
        "Я - Бот Газпром газораспределение и межрегионгаз Ростов-на-Дону,"
        " бот созданный чтобы оперативно помочь Вам. Для продолжения нажмите на кнопку.",
        reply_markup=mr_start
    )


@dp.message_handler(text=back_text)
async def back_command(message: types.Message):
    await start_command(message)


@dp.message_handler(text=gro_text)
async def gro_command(message: types.Message):
    await message.answer(
        "Для продолжения нажмите на кнопку.",
        reply_markup=mr_gro
    )


@dp.message_handler(text=rkg_text)
async def rkg_command(message: types.Message):
    await message.answer(
        "Для продолжения нажмите на кнопку.",
        reply_markup=mr_rkg
    )


# gro
@dp.message_handler(text=gro_contract)
async def gro_contract_command(message: types.Message):
    await message.answer(
        gro_contract
    )


@dp.message_handler(text=gro_planned_date)
async def gro_planned_date_command(message: types.Message):
    await message.answer(
        gro_planned_date
    )


@dp.message_handler(text=gro_amount_debt)
async def gro_amount_debt_command(message: types.Message):
    await message.answer(
        gro_amount_debt
    )


@dp.message_handler(text=gro_applic_same)
async def gro_applic_same_command(message: types.Message):
    await message.answer(
        gro_applic_same
    )


@dp.message_handler(text=gro_price_list)
async def gro_price_list_command(message: types.Message):
    await message.answer(
        gro_price_list
    )


@dp.message_handler(text=gro_safety_rules)
async def gro_safety_rules_command(message: types.Message):
    await message.answer(
        gro_safety_rules
    )


@dp.message_handler(text=gro_contact)
async def gro_contact_command(message: types.Message):
    await message.answer(
        gro_contact
    )


@dp.message_handler(text=gro_applic_same)
async def gro_applic_same_command(message: types.Message):
    await message.answer(
        gro_applic_same
    )


@dp.message_handler(text=gro_inretact_map)
async def gro_inretact_map_command(message: types.Message):
    await message.answer(
        gro_inretact_map
    )


# rkg
@dp.message_handler(text=rkg_amount_debt)
async def rkg_amount_debt_command(message: types.Message):
    await message.answer(
        rkg_amount_debt
    )


@dp.message_handler(text=rkg_date_amount)
async def rkg_date_amount_command(message: types.Message):
    await message.answer(
        rkg_date_amount
    )


@dp.message_handler(text=rkg_date_value)
async def rkg_date_value_command(message: types.Message):
    await message.answer(
        rkg_date_value
    )


@dp.message_handler(text=rkg_transm_meter_read)
async def rkg_transm_meter_read_command(message: types.Message):
    await message.answer(
        rkg_transm_meter_read
    )


@dp.message_handler(text=rkg_list_doc)
async def rkg_list_doc_command(message: types.Message):
    await message.answer(
        rkg_list_doc
    )


@dp.message_handler(text=rkg_req_cont_reasons)
async def rkg_req_cont_reasons_command(message: types.Message):
    await message.answer(
        rkg_req_cont_reasons
    )


@dp.message_handler(text=rkg_about_proced_gaz)
async def rkg_about_proced_gaz_command(message: types.Message):
    await message.answer(
        rkg_about_proced_gaz
    )


@dp.message_handler(text=rkg_about_term_contr)
async def rkg_about_term_contr_command(message: types.Message):
    await message.answer(
        rkg_about_term_contr
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
