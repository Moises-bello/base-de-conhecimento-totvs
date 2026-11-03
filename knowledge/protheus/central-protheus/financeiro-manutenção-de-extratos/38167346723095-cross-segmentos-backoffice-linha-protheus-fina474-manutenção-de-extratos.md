---
article_id: 38167346723095
category: Financeiro - Manutenção de Extratos
content_hash: 60bad6e1b27201792b5cf5fa378d45b72dcaa25e01306c9c82b638110a9db34b
fetched_at: '2026-06-28T22:37:31.142265+00:00'
product: protheus
section_id: 35057672519319
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINA474 - Manutenção de extratos
type: support-article
updated_at: '2026-04-01T16:38:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38167346723095-Cross-Segmentos-Backoffice-Linha-Protheus-FINA474-Manuten%C3%A7%C3%A3o-de-extratos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38167346699287) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Como configurar e importar o arquivo de extrato?  
  
**Ambiente**  
Cross Segmento - TOTVS BackOffice (Linha Protheus) - FINA474 - A partir da versão 12.1.33.  
  
**Solução**  
Para iniciar a configuração, é necessário realizar os cadastros obrigatórios no sistema.

**1º Cadastro – Banco:**  
Preencher os campos obrigatórios: banco, número da agência, dígito da agência (se aplicável), número da conta e dígito da conta (se aplicável).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38167753357463)

2º Cadastro de parâmetros de banco

Preencher os campos obrigatórios: Filtrar o banco cadastrado anteriormente, subconta, extensão, formato de data, bytes de extrato, tamanho de ocorrência e tamanho do motivo de banco. Observação: os últimos campos são padrões.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38167753358359)

3º Na rotina de Manutenção de Extrato, selecione a opção **Importar** e preencha os parâmetros necessários: filtrar o banco, informar a subconta e definir um nome para a importação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38167791380887)

Ao clicar em **Avançar**, deverão ser informados o arquivo de configuração (layout) e o arquivo de extrato (fornecido pelo banco).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38167791382935)

Após o processamento, o sistema exibirá a mensagem de **extrato importado com sucesso**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38167791385879)

Ao visualizar o arquivo importado, serão apresentados os dados do banco, o caminho dos arquivos e a relação dos registros do extrato bancário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38167753369879)

**Vídeos de Apoio:**

* [How To | SIGAFIN - FINA475 - Configuração e Importação 1/2](https://www.youtube.com/watch?v=Liw4N3h3nkQ&ab_channel=TOTVSGest%C3%A3o)
* [How To | SIGAFIN - FINA475 - Configuração e Importação 2/2](https://www.youtube.com/watch?v=cDFjw4mBWGo)
* [How To | SIGAFIN - FINA475 - Configuração JOB](https://www.youtube.com/watch?v=EoxoopQZzxs)
* [How To | SIGAFIN - FINA475 - Configuração de Credenciais](https://www.youtube.com/watch?v=-qU2Wg7sK8s&ab_channel=TOTVSGest%C3%A3o)

**Saiba mais**

[FINA474 - Manutenção de Extratos Bancários](https://tdn.totvs.com/pages/releaseview.action?pageId=721003882)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA475 - Configuração do Retorno de Extratos Bancários Automático](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29588159318039-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA475-Configura%C3%A7%C3%A3o-do-Retorno-de-Extratos-Banc%C3%A1rios-Autom%C3%A1tico)
