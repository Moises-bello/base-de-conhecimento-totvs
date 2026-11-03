---
content_hash: 15bf9c25660f3de58b15cc4f9f862bfa0cf014e420928de6097269c4ef68b54c
fetched_at: '2026-06-29T00:11:36.725609+00:00'
page_id: '773505798'
product: rm
source: tdn-rm
title: 'DT - Parametrizador: Retirado do parâmetro "Diretório utilizado para processos
  que geram arquivos em .Net (Job)Server"'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=773505798
version: 25
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Parametrizador |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-6553](https://jiraproducao.totvs.com.br/browse/DRHROTRM-6553) |

## **01. VERSÕES**

**A partir da Versão:**

* 12.1.2306.119

## **02. SITUAÇÃO/REQUISITO**

Anteriormente, contávamos com o parâmetro "DiretorioArqNet" que nos permitia selecionar um diretório específico para salvar os arquivos temporários no servidor. Era como se fosse um endereço físico no computador, onde o sistema sabia exatamente onde guardar os arquivos que eram enviados ou criados dentro do servidor.

Veja detalhes do processo anterior no [TDN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037728134-RH-RM-FOP-Corre%C3%A7%C3%A3o-de-erros-na-execu%C3%A7%C3%A3o-de-rotinas-que-geram-arquivos)

## **03. SOLUÇÃO**

Passamos por uma modernização, para garantir escalabilidade e compatibilidade com cloud, e agora ele é capaz de identificar automaticamente o local mais adequado para salvar esses arquivos. Isso significa que não precisamos mais definir manualmente esse diretório, pois o sistema agora cuida disso.

O RM agora será responsável por identificar e definir automaticamente o local adequado para salvar os arquivos, levando em consideração todas as melhorias que foram implementadas.

**Exemplo referente ao comportamento em patches anteriores ao informado no item 01:**

Anteriormente, quando o usuário informava o caminho "D:\Servidor\Geral" e gerava a SEFIP, o sistema gravava o arquivo SEFIP.RE da seguinte forma:

D:\Servidor\Geral\Coligada(X)\SEFIP.RE

Onde (X) é o código da Coligada, e a pasta Coligada(X) era gerada automaticamente pelo processo, sem influência de parâmetros.

**Exemplo referente ao comportamento após a aplicação dos patches informado no item 01:**

Quando a tag <FILESERVERPATH> NÃO estiver preenchida:

Nesse caso, o sistema determinará o diretório raiz com base no local onde está instalado, para compor o caminho do arquivo:

Diretório Raiz onde o host se encontra + Arquivos + Pasta criada pelo processo + nome do arquivo

Portanto, se o host estiver instalado em C:\TOTVS\Corpore.Net, o arquivo ficará em: C:\TOTVS\Corpore.Net\Arquivos\Coligada(X)\SEFIP.RE

Quando a tag <FILESERVERPATH> estiver preenchida com um caminho válido:

Supondo que a tag FILESERVERPATH esteja configurada com o valor "\\server\source\files".

Ao gerar a SEFIP, o sistema gravará o arquivo SEFIP.RE no seguinte caminho:  \\server\source\files\Coligada(X)\SEFIP.RE

**Observações adicionais:**

* + A criação da pasta Coligada(X) faz parte do processo e não está relacionada à configuração do parâmetro FILESERVERPATH.

**ATENÇÃO:**

A pasta compartilhada era exclusivamente usada internamente pelo produto para a transferência de arquivos.

Os processos que faziam uso desse caminho incluíam: SEFIP, GRRF, Folha Analítica, Homolognet, Seguro Desemprego, RAIS, CAGED, MANAD, ESocial, Esocial (Qualificação Cadastral), Cálculo Férias Coletivas, Cálculo Rescisão, Cálculo do Orçamento, Cancelamento de Movimento e Aviso Prévio Coletivo.

Ao gerar as rotinas da Folha de Pagamento, os arquivos eram disponibilizados no caminho indicado durante a geração das rotinas, em vez de serem salvos na pasta especificada no Parametrizador da Folha de Pagamento. Isso ocorre porque a pasta compartilhada era reservada exclusivamente para a transferência interna de arquivos pelo produto.

Essa condição permanece inalterada, ou seja, continua disponibilizando os arquivos no caminho indicado durante a geração das rotinas.

**OBSERVAÇÃO:**

* Caso haja necessidade de especificar manualmente esse diretório, é possível utilizar o parâmetro FILESERVERPATH no arquivo rm.host.exe.config, porém é recomendável deixar o RM decidir.
* Ao preencher o FILESERVERPATH, é essencial garantir que o caminho seja válido e que o host possua as devidas permissões para operar, no mínimo, permissões de leitura e escrita na pasta especificada.
* É importante lembrar que essa alteração se refere ao diretório do servidor e não afeta as especificações de download de arquivo para a máquina local do cliente.
