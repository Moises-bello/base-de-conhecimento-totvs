---
article_id: 1500000890822
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 01258d38ad449c16d2f2e503b437cbc8626633a13e18a56936201dfc9361362a
fetched_at: '2026-06-28T22:37:55.155858+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN  - FINA420 - HELP - F420CRIA
type: support-article
updated_at: '2025-07-09T11:58:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000890822-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA420-HELP-F420CRIA
---

**Ocorrência**

No momento de gerar arquivo de saída no **Arquivo de Pagamentos (FINA420),** apresenta o **HELP: F420CRIA**

**![imagem1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101844453/imagem1.png)**

**Ambiente**Microsiga Protheus – Financeiro – A partir da versão 12.1.17

**Causa**Este erro ocorre ao tentarmos informar o caminho onde serão gravados o arquivo de envio a pagar do CNAB

**Solução**

Existem parâmetros que fazem o processo da rotina, sendo obrigatório informar o nome do arquivo.

Os parâmetros **MV\_LOCENV**e **MV\_LOCREC**, definem os diretórios que são gravados os arquivos de CNAB, de envio e de recebimento.

Validar o caminho dos arquivos de remessa e retorno através dos parâmetros: **MV\_LOCENV** e **MV\_LOCREC.   
  
Exemplo:**C:\TOTVS12127\protheus\_data\system\

Na rotina **FINA420** > Pergunta: **Arq. de Configuracao ?** Informe somente o nome do arquivo .extensão. Este é o arquivo que foi gravado as configurações de parametrização do CNAB no Módulo **Configurador**.

Na rotina **FINA420** > Pergunta: **Arq. de Saída ?** Informe **somente o nome do arquivo de envio .extensão** e verifique se o mesmo será gerado no caminho informado pelos parâmetros.  
  
Obs:

O Protheus não permite a utilização de caminhos de rede sem uma unidade local mapeada, como por exemplo: **\\1.1.1.1\porta.**  
Caminhos desse tipo, como links diretos de SharePoint ou pastas de rede não mapeadas, não são reconhecidos corretamente pela aplicação.

Para funcionar corretamente, é necessário mapear a unidade de rede **(ex: atribuir uma letra como Z:\) antes de utilizá-la no sistema.**

**Saiba mais:**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=242386580>  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005056031-MP-SIGAFIN-CNAB-Help-F150ARQ>
