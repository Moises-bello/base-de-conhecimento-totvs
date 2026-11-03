---
article_id: 18396513857559
category: Materiais - Compras (SIGACOM)
content_hash: 8add5db99f783e3b9e7373545715962984c116b81ac7b6012a6713fda8be5d05
fetched_at: '2026-06-28T22:41:12.732846+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGACOM  - Gravar Origem
  + CST quando documento é originado via Importador XML
type: support-article
updated_at: '2025-01-03T14:33:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18396513857559-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Gravar-Origem-CST-quando-documento-%C3%A9-originado-via-Importador-XML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18396544583703) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Como gravar a Origem + CST quando documento é originado via TOTVS Colaboração / Importador XML? 

**Ambiente**

## Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - versão 12

**Solução**

Segue a explicação sobre a funcionalidade de gravação de origem e **CST** no Protheus, especificamente para os campos **DT\_CLASFIS** e **D1\_CLASFIS**, com base no parâmetro **MV\_COLCFIS**:

**Configuração do parâmetro MV\_COLCFIS.**  
  
Formato do conteúdo: Deve ser configurado no formato de=para, utilizando o caractere | como separador entre os pares.

Exemplo: 0 = 0 | 1 = 2 | 2 = 1 | 5 = 5

Neste exemplo:

Origem 0 será mapeada para 0.  
Origem 1 será mapeada para 2.  
Origem 2 será mapeada para 1.  
Origem 5 será mapeada para 5.

**Configuração vazia:** se o parâmetro for deixado vazio, o sistema adotará o comportamento padrão.

Ele preencherá automaticamente os campos de classificação fiscal (**DT\_CLASFIS** e **D1\_CLASFIS**) concatenando a tag do ICMS com a origem do item.

**Gravação dos Campos:**  
**DT\_CLASFIS** (Origem): O campo será preenchido conforme a origem do documento ou conforme a regra definida no parâmetro **MV\_COLCFIS**.  
  
**D1\_CLASFIS** (Classificação Fiscal): O preenchimento do campo **D1\_CLASFIS** segue a mesma lógica do campo **DT\_CLASFIS**, mas sem os valides (regras de validação associadas).  
  
**Comportamento Padrão:**  Origem da Tag do ICMS: Quando o parâmetro **MV\_COLCFIS** está vazio, o sistema usará a tag correspondente ao ICMS e concatenará com a origem para gerar a classificação fiscal.  
  
**Observação:**

A configuração precisa ser validada em ambiente de testes antes da aplicação no ambiente produtivo.

Caso algum comportamento inesperado ocorra, é necessário verificar os logs do sistema para identificar a origem do problema e ajustar o parâmetro ou a configuração da integração.

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Os documentos não estão aparecendo na rotina do monitor (COMXCOL).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20435145226135)

[Regras TES / CONDIÇÃO DE PAGAMENTO](https://tdn.totvs.com.br/pages/viewpage.action?pageId=546695598)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
