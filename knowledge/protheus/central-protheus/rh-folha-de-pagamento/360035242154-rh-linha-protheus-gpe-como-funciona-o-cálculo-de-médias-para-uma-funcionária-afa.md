---
article_id: 360035242154
category: RH - Folha de Pagamento
content_hash: 9b208acd3a5f13393239968e3739d19309eee2ed82936756c3ffea594b8d2a77
fetched_at: '2026-06-28T22:44:13.514618+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como funciona o cálculo de médias para uma funcionária
  afastada em licença maternidade
type: support-article
updated_at: '2025-04-22T21:15:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035242154-RH-Linha-Protheus-GPE-Como-funciona-o-c%C3%A1lculo-de-m%C3%A9dias-para-uma-funcion%C3%A1ria-afastada-em-licen%C3%A7a-maternidade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17818623879831) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como funciona o cálculo de médias para uma funcionária afastada em licença maternidade?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A forma de cálculo do Salário-maternidade, está definida nos artigos 71 a 73 da Lei 8.213/91.  
  
Para a empregada ou trabalhadora avulsa, a Lei determina que o valor do benefício seja no mesmo valor da sua remuneração integral equivalente a um mês de trabalho. O valor máximo a ser pago, deverá obedecer o limite fixado no artigo 37, XI da Constituição Federal, nos termos do artigo 248 do mesmo diploma legal.  
  
Caso a remuneração da empregada ou trabalhadora avulsa seja, parcialmente ou totalmente variável, será obedecido ainda o seguinte critério:  
- **Será considerada a média aritmética simples dos 6 últimos salários,** apurada de acordo com o valor definido para a categoria profissional em lei ou dissídio coletivo, excetuando-se para esse fim, o décimo terceiro salário, adiantamento de férias, e as rubricas constantes do parágrafo 9º do artigo 214 do Decreto 3.408/99.  
- Entende-se como parcialmente variável, a remuneração constituída de parcelas fixas e variáveis.  
- Entende-se como variável, a remuneração constituída somente de parcelas variáveis.  
  
Desta forma, no ambiente Gestão de Pessoal, em **Atualizações > Definições de Cálculo > Verbas (GPEA040)**, deve ser criada uma verba para o **identificador 0407 - Pagamento das Médias Aux. Maternidade.** A busca das verbas para compor a média  será efetuada de acordo com a incidência do campo **Incidência das Médias para Férias** (RV\_MEDFER), da Tabela de Verbas (SRV).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31594650309527)  
Assim, somente serão somadas as verbas cujo conteúdo deste campo estiver com **S** ou **SP**, ou o número de meses para média.  **Exemplo**: Verba de Hora Extra com S para médias férias.  
  
Na rotina Tipos de Ausências em **Atualizações > Definições de Cálculos > Tipo de Ausências (GPEA430)**, no **Tipo de Ausência 006** também é possível parametrizar os meses para busca dos valores que farão base para o cálculo das médias de licença maternidade, no padrão esse campo vem preenchido com 6, mas é possível alterar de acordo com a necessidade de busca dos meses:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31594650311959)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31594650312855)

Para realizar a conferência, gerar o demonstrativo de médias diretamente na rotina de **Lançamentos Por Funcionário (GPEA580)   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31594681049623)**  
  
**Observação:**  
Este identificador (0407) foi criado exclusivamente para o pagamento das médias para funcionárias com salário não variável. Somente será utilizada quando o campo **Categoria** (RA\_CATFUNC), do Cadastro de Funcionários for **diferente** de [C]omissionado e [T]arefeiro. Vale lembrar que, para estes casos, o pagamento é efetuado na própria verba de pagamento do auxílio maternidade (Identificador 0040).

**Saiba Mais:**[RH - Linha Protheus - GPE - Prorrogação da Licença Maternidade](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhqtjnTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyNjA2MDM5NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUHJvcnJvZ2ElQzMlQTclQzMlQTNvLWRhLUxpY2VuJUMzJUE3YS1NYXRlcm5pZGFkZQY7CFQ6DnNlYXJjaF9pZEkiKWE4ZTkzY2FkLTY4NGQtNDE3Mi1iYjIwLTEwZjY1Y2Q0NDNmZgY7CEY6CXJhbmtpCDoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiGWxpY2Vuw6dhIG1hdGVybmlkYWRlBjsIVDoScmVzdWx0c19jb3VudGkCGAQ%3D--df9ae650fd3145ac78bf9b0f1db3aac1586c9529)  
[RH - Linha Protheus - GPE - Adicionais Prorrogação Licença Maternidade](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXyx7JwQk6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBmGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzEwNzI3OTA3NTc2NzI3LVJILUxpbmhhLVByb3RoZXVzLUdQRS1BZGljaW9uYWlzLVByb3Jyb2dhJUMzJUE3JUMzJUEzby1MaWNlbiVDMyVBN2EtTWF0ZXJuaWRhZGUtBjsIVDoOc2VhcmNoX2lkSSIpYThlOTNjYWQtNjg0ZC00MTcyLWJiMjAtMTBmNjVjZDQ0M2ZmBjsIRjoJcmFua2kPOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIZbGljZW7Dp2EgbWF0ZXJuaWRhZGUGOwhUOhJyZXN1bHRzX2NvdW50aQIYBA%3D%3D--f846dc2c63d4b13812887a0cad4cbd5f39ffec1c)  
[RH - Linha Protheus - GPE - Como lançar ausência por Licença Maternidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053399713-RH-Linha-Protheus-GPE-Como-lan%C3%A7ar-aus%C3%AAncia-por-Licen%C3%A7a-Maternidade-?source=search)  
[RH - Linha Protheus - GPE - Como configurar Licença Maternidade por Adoção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051079813-RH-Linha-Protheus-GPE-Como-configurar-Licen%C3%A7a-Maternidade-por-Ado%C3%A7%C3%A3o?source=search)  
[RH - Linha Protheus - GPE - Geração de médias na licença maternidade por adoção (ID 1894)](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXy5RQGgk6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBuGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzEwMDA4NjI1NzI4NDA3LVJILUxpbmhhLVByb3RoZXVzLUdQRS1HZXJhJUMzJUE3JUMzJUEzby1kZS1tJUMzJUE5ZGlhcy1uYS1saWNlbiVDMyVBN2EtbWF0ZXJuaWRhZGUtcG9yLWFkbyVDMyVBNyVDMyVBM28tSUQtMTg5NC0GOwhUOg5zZWFyY2hfaWRJIik5OWYzZmYzOC1jMjQzLTQ1NTQtYjFiYi03OWI1MzllNWEyOTQGOwhGOglyYW5raQg6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhdtw6lkaWEgbWF0ZXJuaWRhZGUGOwhUOhJyZXN1bHRzX2NvdW50aQKRBg%3D%3D--0277553b650300aa4adff88601ecaddaa23cffb8)
