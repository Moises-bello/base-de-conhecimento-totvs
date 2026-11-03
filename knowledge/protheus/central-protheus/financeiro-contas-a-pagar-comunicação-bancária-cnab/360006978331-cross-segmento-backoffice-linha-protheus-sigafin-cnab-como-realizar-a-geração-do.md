---
article_id: 360006978331
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 890315132eb64ce9b7ff4296691352aaeef53a266adcf45fe69377295a907678
fetched_at: '2026-06-28T22:37:55.166038+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - CNAB - Como realizar
  a Geração do Arquivo de Retorno - Modelo 2
type: support-article
updated_at: '2021-10-13T17:44:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006978331-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-CNAB-Como-realizar-a-Gera%C3%A7%C3%A3o-do-Arquivo-de-Retorno-Modelo-2
---

**Dúvida**Como realizar a Geração do Arquivo de Retorno - Modelo 2?  
  
**Ambiente**Cross Segmento - BackOffice Linha Protheus – Financeiro – A partir da versão 11.80

**Solução**Gerar o **Arquivo de Retorno** da mesma forma que o **Arquivo de Envio**, porém o modelo deve ser preenchido com a respectiva posição contida no segmento.

Exemplo:  
Se o conteúdo da posição referente ao segmento do arquivo texto for A, o campo modelo também deve ser preenchido com essa opção.

**Mensagens de Ocorrências**Ao definir a formatação dos arquivos (**Remessa e Retorno**), é necessário informar as mensagens de ocorrências utilizadas pelo Banco para a transmissão bancária e os parâmetros adicionais para o envio; como: **número do disco**, **valor do** **IOF,** etc.

As informações das ocorrências e dos parâmetros devem ser realizadas no módulo **Financeiro** através das opções Ocorrências CNAB e Parâm. Bancos-CNAB, assim como, a geração dos arquivos de remessa e retorno.

**Segmento J-52**1. Crie ou Restaure o arquivo de configuração (\*.2PR)  
2. No segmento **J-52** pressione a **tecla [F4]** para acessar os detalhes  
3. Configure o segmento conforme o manual do banco  
4. Na linha que identifica o segmento **J-52**, preencha a coluna conteúdo com o valor **SEGJ52**.  
5. Confirme a operação e salve o arquivo.

**Veja mais**

* [Página Centralizadora do CNAB](http://tdn.totvs.com/display/PROT/CNAB)
* [Como Parametrizar o sistema para a geração do CNAB](https://centraldeatendimento.totvs.com/hc/pt/articles/360006611532-MP-SIGAFIN-CNAB-Como-parametrizar-o-sistema-para-gera%C3%A7%C3%A3o-do-CNAB-)
* [Principais mensagens do CNAB](http://tdn.totvs.com.br/pages/viewpage.action?pageId=353280222)
