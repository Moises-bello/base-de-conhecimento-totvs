---
content_hash: 1efdc30d9345f5f9c10f4c0e46e9323216f12fd35bf4ab98d86784f165cb63c4
fetched_at: '2026-06-29T00:10:03.631120+00:00'
page_id: '452719101'
product: rm
source: tdn-rm
title: Cópia de Horário entre Coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719101
version: 92
---

Este processo possibilita copiar os horários existentes para outra coligada. Todos os dados do horário serão copiados .Serão listadas caso houver todas as coligadas disponíveis na base de dados para se fazer à cópia do(s) registro(s). Selecione a(s) coligada(s) para a qual deseja fazer a cópia.

O parâmetro 'Substitui registros no destino se eles já existirem' quando habilitado irá substituir o horário de mesmo código da coligada de destino pelo horário da coligada de origem.

Se o horário da coligada de destino possui Limite de Tolerância, quando for realizada a cópia do horário entre coligadas ao confirmar para substituir o limite de tolerância será sobrescrito também , inclusive as tolerâncias existentes em outros horários.

Para que seja realizada a substituição o usuário deverá confirmar a pergunta: 'Existem limites de tolerâncias a serem alterados na coligada destino' e ' Existem registros para este horário na Coligada destino. Deseja substituir os registros por este? O usuário irá selecionar Sim ou Não conforme necessidade.

No processo de cópia de horário entre coligadas, será realizada também a cópia da [Pausa Remunerada](https://tdn.totvs.com/display/LRM/Pausa+Remunerada).

**Exemplo 2:** Parâmetro 'Substitui registros no destino se eles já existirem', marcado e com Limite de tolerância  
Usuário deseja realizar a cópia do horário 0001 da coligada 1 que tem os limites códigos: 0001,0002 e 0003 e número de horas 00:10.Essa cópia será feita para a coligada 6 com o parâmetro 'Substitui registros no destino se eles já existirem' habilitado. Porém na Coligada 6 existe também o horário 0001 com os limites 0001 e 0002 e número de horas 00:15. Ao realizar a cópia o horário 0001 da Coligada 6 será substituído pelo horário 0001 da coligada 1 , inclusive todos os horários que tiverem o mesmo código limite de tolerância serão sobrescritos. Caso o parâmetro 'Substitui registros no destino se eles já existirem' não for habilitado será mantido.
