---
article_id: 4403487186455
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: c3eb773e6e4ef655027ab8107b23be8bd6f91893a373cf3b3aa4ad34a8a232a8
fetched_at: '2026-06-28T22:42:05.049119+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuição
  configuração para não gerar NF cancelada no mesmo mês da emissão no arquivo txt
type: support-article
updated_at: '2022-08-31T13:14:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403487186455-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%A3o-configura%C3%A7%C3%A3o-para-n%C3%A3o-gerar-NF-cancelada-no-mesmo-m%C3%AAs-da-emiss%C3%A3o-no-arquivo-txt
---

**Dúvida**

Como configurar o sistema para não gerar NF cancelada no arquivo **EFD Contribuições** quando o cancelamento ocorreu no mesmo mês da emissão da NF.  
  
**Ambiente**  
Cross Segmento - Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
Para não gerar a NF cancelada no arquivo txt do EFD Contribuições, é necessário configurar o parâmetro **MV\_C100CAN;**

Escrituração das notas **Canceladas, Inutilizadas e Denegadas**:

|  |  |
| --- | --- |
| Nome da Variável | MV\_C100CAN |
| Tipo | Lógico |
| Conteúdo | T |
| Descrição | Controle para escrituração ou não de notas canceladas, SITDOC 02 ou 03, no registro C100 do SPED Pis/Cof. .T. escritura, .F. não escritura. |

Quando o parâmetro está **MV\_C100CAN = .F.**  as numerações **inutilizadas/ canceladas**, não são geradas no **arquivo txt** do **EFD Contribuições**.  
   
Quando o parâmetro está **MV\_C100CAN = .T.** as numerações **inutilizadas/ canceladas**, são geradas no **arquivo txt** do **EFD Contribuições**

**Importante:**

O parâmetro **MV\_C100CAN** também controla a escrituração das **NF** **denegadas** e **inutilizadas**, respectivamente **SITDOC 04** e **05**.

As NF canceladas em períodos posteriores ao mês da emissão, conforme as regras do **Guia Prático do EFD Contribuições**, no mês em que está ativa, a Nota será demonstrada no **arquivo txt** e no mês do cancelamento, ocorrerá um **ajuste** na **Apuração** e consequentemente no **Bloco M**.  
Ou seja, a Nota Fiscal de Saída foi emitida em 31/01, portanto, na competência Janeiro a NF aparecerá como Ativa.  
E como o cancelamento ocorreu em 01/02, na competência Fevereiro, ocorrerá um **ajuste** na **Apuração** que será demonstrado no **Bloco M** do **Arquivo txt**.  
   
A legislação está no **Guia Prático do EFD Contribuições** e nas **perguntas e Respostas da Receita Federal**, que o **Contribuinte** tem acesso.
