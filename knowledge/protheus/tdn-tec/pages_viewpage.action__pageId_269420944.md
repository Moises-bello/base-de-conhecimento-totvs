---
content_hash: 810ecbf32b841ff21da80baada74ff09fc02e8e786d2f30a41e25c3173f0bdc2
fetched_at: '2026-07-02T19:24:22.321010+00:00'
page_id: '269420944'
product: protheus
source: tdn-tec
title: Melhoria - Suporte a Picture Numérica Russa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269420944
version: 2
---

|  |  |
| --- | --- |
| Situação | A picture na Russia é um pouco diferente dos padrões: 999 999 999,99 (com espaços separando os milhares), necessário implementar no nosso sistema |
| Ocorrência | A picture numérica é tratada diretamente pelo SmartClient, porém necessitou de alterações na função \_\_SetPicture para aceitar um novo formato. |
| Melhoria | A função \_\_SetPicture agora também aceita a configuração "RUSSIAN", e a partir disso todas as pictures com @E são tratadas como sendo Russas. |
| Informações adicionais | * Referente ao chamado: TWKVNJ * Referente à ocorrência: SSIM-1295 * Disponível no Label 7.00.131227A, release SmartClient 2.3.3 |
