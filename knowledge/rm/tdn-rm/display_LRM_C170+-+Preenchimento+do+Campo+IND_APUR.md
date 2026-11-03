---
content_hash: cd49a12a299aa9967c099d57e6e8c56dbe5f01519e55f9c2efc208bae4a74574
fetched_at: '2026-06-29T00:11:21.309121+00:00'
page_id: '691469548'
product: rm
source: tdn-rm
title: C170 - Preenchimento do Campo IND_APUR
type: documentation
url: https://tdn.totvs.com/display/LRM/C170+-+Preenchimento+do+Campo+IND_APUR
version: 5
---

#f5f5f5#363636nonePreenchimento do campo IND\_APUR

## **01. Visão GeralVisaoGeral**

O campo "IND\_APUR", do registro C170 da EFD Contribuições, é preenchido de acordo com a periodicidade do IPI informada no produto. Esse parâmetro pode ser acessado em Obrigações Principais > Períodos de Apuração > Selecione o período de IPI desejado > Código do Tributo > Periodicidade. Para acessar esse parâmetro dentro de um lançamento fiscal, vá no cadastro do produto > Anexos > Tributos do Produto. Cadastre ou acesse um período do IPI, edite-o e vá em Código do Tributo e informe o valor desejado no campo Periodicidade.

Lembre-se

Ao alterar a periodicidade do IPI, ela não será alterada somente para o período ou produto na qual foi editada, mas sim para todos os períodos de apuração do IPI.

## **02. Origem dos Dados****ArquivosDisponiveis**

Na geração da rotina, o campo IND\_APUR possui apenas dois valores, sendo 0 quando a periodicidade é preenchida como Mensal, e 1 quando é preenchida como Decendial. Caso qualquer outro valor seja informado na periodicidade, o campo também será gerado com o valor 0.

É importante destacar que o comportamento e valor de preenchimento deste campo é igual ao campo 19 (IND\_APUR), do registro de mesmo nome, do SPED Fiscal.  
Porém, apenas alguns campos (como é o caso do IND\_APUR) têm comportamentos semelhantes nas duas rotinas, não devendo ser considerada a total equidade de todos os campos dos registros C170 na EFD Contribuições e no SPED Fiscal.

#f5f5f5#feac0eDocumentos Relacionados10%90%10%90%10%90%10%90%

**(Registro C100)**
