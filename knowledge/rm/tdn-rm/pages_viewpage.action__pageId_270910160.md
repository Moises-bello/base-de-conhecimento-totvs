---
content_hash: 8d09bbc9e17e87e4ce437aac724e31f1d6b244b89e2471d9e1e8bedf0ecedf56
fetched_at: '2026-06-29T00:08:25.035167+00:00'
page_id: '270910160'
product: rm
source: tdn-rm
title: RMEDU00001_Concessão de bolsas futuras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270910160
version: 4
---

# Concessão de Bolsas Futuras

|  |  |
| --- | --- |
| **Produto:** | Gestão Educacional |
| **Versões:** | 12.1.14 |
| **Processo:** | Concessão de bolsas futuras |
| **Data da publicaç****ão:** |  |

A concessão de bolsa futura permite a instituição fazer o planejamento de quais bolsas serão disponibilizadas a determinados alunos de acordo com as regras de negócio.

Durante a inserção de um novo contrato o sistema verifica se existe bolsas futuras planejadas para aquela habilitação e automaticamente inclui as bolsas previstas.

Para que a bolsa seja incluída automaticamente, no processo de rematrícula é necessário que no cadastro da bolsa, no anexo: bolsas por período letivo, o período letivo para qual o aluno está sendo matriculado, esteja incluído.

O sistema irá levar em consideração a data de vencimento da parcela e não da assinatura do contrato para conceder a bolsa para a parcela. Portanto, qualquer inclusão/alteração de parcelas no contrato, o sistema irá verificar se existe concessão para aquela parcela. Irá levar em consideração se o vencimento está dentro do período da concessão.

Financeiro/contábil | formação de preço | bolsas | concessão de bolsas futuras

Preencha para qual aluno, será concedida a bolsa, qual bolsa será concedida, qual a data de validade inicial e final para essa bolsa e qual será o tipo de desconto (percentual ou valor).

Se o parâmetro "**Inserir bolsa automaticamente**" estiver desabilitado, o sistema não realizará o cadastro da bolsa para o aluno no momento de cadastro do contrato, necessitando que o usuário informe a bolsa para o aluno de forma manual.

No anexo: habilitação da concessão de bolsas futuras do cadastro, preencha a matriz aplicada, a qual o aluno terá direito a receber a bolsa. É primordial definir qual será a matriz aplicada correspondente, sem a definição da habilitação da concessão da bolsa não é possível o cadastro da bolsa no contrato do aluno.

No anexo: serviços da concessão de bolsas futuras do cadastro, preencha o serviço que terá direito a utilizar a bolsa.

Caso a concessão de bolsa seja cadastrada com o parâmetro "**Todos os serviços**" marcado, não será necessário informar o serviço específico, pois todos serviços receberão o benefício

Currículo e oferta | oferta | parametrização por curso | anexo: configuração de matricula

Na parametrização por curso da matriz do aluno, o plano de pagamento com as parcelas devem ser informadas, para que a bolsa seja inserida no contrato.

Configurações | parâmetros | tesouraria | geral 2/2

Caso o plano de pagamento default, esteja bloqueado para seleção, verifique a parametrização dos sistema. Se o modelo do plano de pagamento for por período da matriz aplicada, a informação de plano "default", é cadastrada no próprio plano de pagamento para cada período da matriz.

Matrícula e avaliação | matrícula | rematricula

Ao realizar o processo de rematricula, após finalizado, é possível verificar que a bolsa é inserida automaticamente para o aluno.

Observação: o parâmetro: cadastrar contrato financeiro, deve ser marcado no processo.
