---
article_id: 24323706068119
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 2b8f31a12569fd7e77328e547e409bcde4e4d01412790c73077bdc132aa45116
fetched_at: '2026-06-28T22:42:10.709397+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DCTF- R10 -
  Campo 06 - Grupo de Tributo - Erro - Grupo de Tributo não pode ser "11" se Ano do
  Período de Apuração posterior a 2023.
type: support-article
updated_at: '2024-06-21T17:18:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24323706068119-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DCTF-R10-Campo-06-Grupo-de-Tributo-Erro-Grupo-de-Tributo-n%C3%A3o-pode-ser-11-se-Ano-do-Per%C3%ADodo-de-Apura%C3%A7%C3%A3o-posterior-a-2023
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24323720582807) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao validar o arquivo da **DCTF** é apresentado o seguinte erro de validação

**Campo 06 - Grupo de Tributo - Erro - Grupo de Tributo não pode ser "11" se Ano do Período de Apuração posterior a 2023.**

**Ambiente**TOTVS Backoffice (Linha Protheus) – Livros Fiscais – Todas as versões.

**Causa**

Contribuintes de **ICMS**precisa gerar e enviar o arquivo **DCTF** sem considerar os códigos de retenção de  **5952 - (CSRF)** para atender a instrução normativa **RFB nº 2137**, de **21 de março de 2023**.

**Solução**

Para solução desta ocorrência na geração do arquivo na rotina **MATA978,** deve-se utilizar  parâmetro **MV\_DCTFEXC** para não considerar os códigos de retenção de **5952 - (CSRF).** Para desconsiderar os códigos listados na geração do arquivo do **DCTF**.

**Parâmetro:**

|  |  |
| --- | --- |
| **Nome** | MV\_DCTFEXC |
| **Tipo** | Caracter |
| **Conteúdo** | <definido pelo cliente> |
| **Descrição** | Indica os códigos de retenção que não serão considerados para geração da DCTF |
| **Exemplo** | Exemplo: '3746','3770','5960','5979','5987','7460','7485','7498','8047','5952' |

Atualizações da rotina DCTF - **MATA978**:

[Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DCTF - Atualização dos Fontes](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhERsnSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBp2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxODY5MTY1Mi1Dcm9zcy1TZWdtZW50b3MtQmFja29mZmljZS1Qcm90aGV1cy1GSVMtQXJxLU1hZ24lQzMlQTl0aWNvcy1EQ1RGLUF0dWFsaXphJUMzJUE3JUMzJUEzby1kb3MtRm9udGVzBjsIVDoOc2VhcmNoX2lkSSIpYjA4ODExM2UtYTRiZS00MzNmLTk1YjEtZjE3ODBiMTVmNTJhBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJkQ3Jvc3MgU2VnbWVudG9zIC0gQmFja29mZmljZSBQcm90aGV1cyAtIEZJUyAtIEFycS5NYWduw6l0aWNvcyAtIERDVEYgLSBBdHVhbGl6YcOnw6NvIGRvcyBGb250ZXMGOwhUOhJyZXN1bHRzX2NvdW50aQLoAw%3D%3D--a42d47687e8eef860d435b2a99b6644f31a84172)

**04. DEMAIS INFORMAÇÕES**

Importante

Para clientes que operam nas releases 12.1.2310 ou anteriores, será necessária a execução do compatibilizador **UPDDISTR** com o pacote **(SDFBRA.TXT).**

Esta correção será disponibilizada na Expedição contínua de 19/04/2024  e o pacote poderá ser acessado através dos links disponibilizados na documentação Pacotes de Atualização - Fiscal.

Informações sobre a Expedição contínua acessar: [http://tdn.totvs.com/x/H4uCEw](https://tdn.totvs.com/x/H4uCEw).

Informações sobre o compatibilizador **UPDDISTR** acessar: Atualizador de dicionário e base de dados - **UPDDISTR.**

## **05. ASSUNTOS RELACIONADOS**

* [DCTF - Declaração dos Débitos e Créditos Tributários Federais](https://tdn.totvs.com/pages/viewpage.action?pageId=655865674)
* [Instrução Normativa RFB nº 2137 de 21 de Março de 2023](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=129699#2422547 "Seguir link")
