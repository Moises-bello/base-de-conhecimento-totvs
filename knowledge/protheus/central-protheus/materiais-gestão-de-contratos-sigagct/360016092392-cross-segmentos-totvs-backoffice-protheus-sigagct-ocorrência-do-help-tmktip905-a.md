---
article_id: 360016092392
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 9a36f1f791506b7c01d754f0b273039b01cd7461a6121248d35674afb4a21765
fetched_at: '2026-06-28T22:37:23.971082+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Ocorrência do Help
  TMKTIP905 ao encerrar uma medição no Uso da Cond. Pagamento Tipo 9
type: support-article
updated_at: '2025-09-02T19:43:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016092392-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Ocorr%C3%AAncia-do-Help-TMKTIP905-ao-encerrar-uma-medi%C3%A7%C3%A3o-no-Uso-da-Cond-Pagamento-Tipo-9
---

**Ocorrência**

Ocorrência do Help TMKTIP905 ao encerrar uma medição.

**Ambiente**

Microsiga Protheus – Gestão de Contratos – A partir da versão 12.1.17  
  
**Causa**

No módulo **Gestão de Contratos**, ao realizar o encerramento da medição é gerada a ocorrência **TMKTIP905**  A quantidade de parcelas não esta compatível. Verificar junto ao administrador do sistema relação entre parâmetro MV\_NUMPARC e dicionário de dados.

Esse incidente ocorre, pois os campos de parcelas e datas de vencimento não foram criados manualmente nas tabelas SC5 e CND de acordo com a quantidade informada no parâmetro MV\_NUMPARC.

No padrão da CND e SC5 existem os campos apenas para a quantidade até 4 parcelas no MV\_NUMPARC, com mostra a imagem abaixo:

CND:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11225512574359)

SC5:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11225597195415)

Dessa forma, se o MV\_NUMPARC for alterado para a Condição de Pagamento "Tipo 9" ser usado com mais parcelas que 4 (conteúdo maior que 4), então devem ser criados mais campos de "Data" e "Parcela", referente ao numero de parcelas colocado no parâmetro.

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse o módulo Configurador;
2. Selecione a opção Base de Dados - Dicionário - Base de Dados;
3. Selecione a opção Dicionário de Dados;
4. Localize as tabelas SC5 e CND;
5. Edite a tabela e crie os campos de data e parcela de acordo com a quantidade informada no parâmetro MV\_NUMPARC;
6. Exemplo: Parcela 10 - CND\_PARCA e Data da parcela 10 - CND\_DATAA.

**Importante**

Observe que a partir da 10º parcela, os campos de parcela e data devem ser referenciados com letras.

***Obs:***

Mesmo que não se utilize Condição de Pagamento do Tipo 9 nos processos do SIGAGCT, caso os **campos** da **tabela CND** não estejam criados de forma ***compatível com o parâmetro MV\_NUMPARC*** o help será apresentado, necessitando assim a criação dos campos **também na tabela CND** conforme o numero de parcelas definido no parâmetro.

***Saiba Mais:***

[FAT0033 - Mensagem TMKTIP905 - A quantidade de parcelas não está compatível](http://tdn.totvs.com/pages/releaseview.action?pageId=225950783)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
