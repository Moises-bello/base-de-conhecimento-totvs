---
article_id: 36494775640343
category: eConsignado (Crédito do Trabalhador)
content_hash: 4fcc80b088a92b6f0576ab335363f443842627ca1c4b38007df8a44566ce6f79
fetched_at: '2026-06-28T22:43:07.337481+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Na importação do arquivo do eConsignado (Crédito
  do Trabalhador), não estão sendo importados todos os empréstimos que constam no
  arquivo
type: support-article
updated_at: '2026-04-06T11:31:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36494775640343-RH-Linha-Protheus-GPE-Na-importa%C3%A7%C3%A3o-do-arquivo-do-eConsignado-Cr%C3%A9dito-do-Trabalhador-n%C3%A3o-est%C3%A3o-sendo-importados-todos-os-empr%C3%A9stimos-que-constam-no-arquivo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36494790621207) Tempo aproximado para leitura: **00:01:30 min**  
  
**Ocorrência**  
Na importação do arquivo do eConsignado (Crédito do Trabalhador), não estão sendo importados todos os empréstimos que constam no arquivo, com a mensagem: **Cadastre uma nova verba para o eConsignado e informe na tabela S154**.

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões

**Causa**  
Esse incidente ocorre quando:

* O sistema **não reconhece** os registros de empréstimos que estão classificados como **Suspensos** , por isso não a utilizará os mesmos códigos de verbas.
* Não existe verbas suficientes cadastradas no Sistema;
* As verbas para o eConsignado **não foram informadas na tabela S154 - Verbas Crédito do Trabalhador**
* As verbas informadas na S154 estão configuradas incorretamente **(Natureza 9253, CP 31 e Emp. Consignado = Sim)**

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Verifique se o colaborador possui empréstimos classificados como **Suspensos.** Caso exista, **crie novas verbas** para os empréstimos, pois o sistema **não permite a duplicação** de verbas existentes em lançamentos por funcionários nessa situação.
   1. Uma verba só será reutilizada caso a situação do empréstimo esteja como **quitado** ou **descontinuado**.
2. Verifique se **todas as verbas** referente ao **eConsignado** foram **informadas** na tabela **S154 - Verbas Crédito do Trabalhador** em **Atualizações > Definições de Cálculo > Manutenção de Tabelas**
3. Realize uma **nova** tentativa de **importação** do arquivo .JSON ou .CSV e valide se todos os empréstimos foram corretamente importados.

**Saiba Mais**

[RH - Linha Protheus - GPE - Importação Crédito do Trabalhador não realiza a validação de verbas já quitadas na rotina de Valores Futuros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35816163879191-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-Cr%C3%A9dito-do-Trabalhador-n%C3%A3o-realiza-a-valida%C3%A7%C3%A3o-de-verbas-j%C3%A1-quitadas-na-rotina-de-Valores-Futuros)

[RH - Linha Protheus - GPE - Importação do arquivo Crédito trabalhador mês atual com mais de um contrato- eConsignado MP(1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33072630601751-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-do-arquivo-Cr%C3%A9dito-trabalhador-m%C3%AAs-atual-com-mais-de-um-contrato-eConsignado-MP-1-292-2025)

[RH - Linha Protheus - GPE - Importação do arquivo Crédito trabalhador mês subsequente ao período de calculo aberto - mais de um contrato - eConsignado MP(1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33519878477463-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-do-arquivo-Cr%C3%A9dito-trabalhador-m%C3%AAs-subsequente-ao-per%C3%ADodo-de-calculo-aberto-mais-de-um-contrato-eConsignado-MP-1-292-2025)

[eConsignado (Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32292829000215-eConsignado-Cr%C3%A9dito-do-Trabalhador)

[Manual Crédito do Trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)
