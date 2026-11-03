---
content_hash: 1c479151059769291e61c76ee79297a464159f3ab7b28764b3c184ea6c01ee47
fetched_at: '2026-06-29T00:05:50.947487+00:00'
page_id: '1046427810'
product: rm
source: tdn-rm
title: Novo Resíduo Via Fórmula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1046427810
version: 1
---

Para implementar o novo resíduo devemos criar um grupo de venda com os componentes de **Correção Monetária**, **Juros de Contrato** e**Resíduo,**conforme imagem abaixo.

**A manutenção da fórmula é de responsabilidade do cliente**

Criar um componente do Tipo Resíduo e sem tipo Parcela, para realizar o cálculo do resíduo nas parcelas.

No componente de Resíduo não precisa realizar nenhuma configuração, pois a regras de cálculo está nas fórmulas que serão associadas ao CM e Juros, se forem o caso de configurar ambas

Existem dois tipos de resíduos :

Resíduo Tradicional :  O resíduo tradicional calcula o resíduo das 12 primeiras parcelas como se fosse o CM normal e armazena seu valores na parcela do plano de financiamento, o seu cálculo respeita a configuração feita no CM e Juros para cada fórmula utilizada. Os valores serão reajustados até o seu pagamento ou ação de reajuste do vencimento. Os valores ficaram na parcela até serem gerados uma parcela manual com o seu valor, que fica na venda => reajuste => gerar parcela de resíduo, só é permitido gerar parcela de resíduo para parcelas que já foram pagas

Resíduo Sobre Saldo Teórico: Este resíduo gerar o valor de todos os reajustes das parcelas a vencer na primeira parcela, depois , no próximo mês ela pega o saldo devedor das próximas parcelas e joga na segunda parcela, a distribuição só ocorre na 12 ou 13 parcela configurada e assim sucessivamente

ComissãoResíduo Tradicional |

Criar um fórmula para o componente de Correção Monetária. **[Clique Aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=1028938894)**

Criar um fórmula para o componente de Juros. **[Clique Aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=1028938948)**

Residuo sobre o saldo teórico |

Criar um fórmula para o componente de Correção Monetária. **[Clique Aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=635969000)**

Criar um fórmula para o componente de Juros. **[Clique Aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=635969112)**

O Contrato é de 01/06/2017 e as regras de reajuste tem o data base de 01/07/2017 para que se tenha o período de reajuste anual todo mês 7 (julho) e a distribuição do resíduo para as próximas parcelas.

O reajuste pode ser executado todo mês, por ser resíduo, ou executado no mês do aniversário. Irei executar o reajuste no próximo aniversário 01/07/2018.

Veja que o resíduo foi calculado nas parcelas de 1 a 13, sendo que as parcelas de 1 a 12 tiveram seu resíduo distribuído para as parcelas superiores a parcela 12  nos campos de CM e Juros. Com isso, os campos de  Data Geração Resíduo e Grupo Resíduo forma preenchidos com os dados do momento da distribuição.

Reajustar o próximo período,

Importante!

**Ao quitar a última parcela em aberto, havendo resíduo calculado sem distribuição, o sistema irá criar uma nova parcela, em um novo grupo com o somatório desses valores.**

**Para isso, crie um componente do Tipo Principal e Tipo Parcela Resíduo(10), para receber a distribuição. Não é para colocar esse componente no plano de financiamento.**
