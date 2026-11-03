---
article_id: 360028124111
category: RH - Soluções para error.log
content_hash: 2f8e09aad12ed7d47b39526142242d7de964a112114126619f492723cf651267
fetched_at: '2026-06-28T22:44:08.822726+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar arquivos para análise de lentidão (performance)
type: support-article
updated_at: '2025-10-10T14:07:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028124111-RH-Linha-Protheus-GPE-Como-gerar-arquivos-para-an%C3%A1lise-de-lentid%C3%A3o-performance
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26425915059863)** Tempo aproximado para leitura: **02:00:00 min**

**Dúvida**Como gerar arquivos par análise de lentidão (performance)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Após toda a verificação de ambiente da empresa referente ao link abaixo, se mesmo assim o problema de performance ainda persistir, será necessário gerar arquivos para análise do suporte:  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017515552-MP-FRAME-Lentid%C3%A3o-no-Prot>,

Para análise de performance é necessário o envio do arquivo de ***Log Profiler*** (indispensável para análise) e o arquivo de **Trace** do *DBaccess*

**Importante:**Antes de gerar qualquer um dos arquivos, será necessário limpar seu conteúdo.  
  
***Log Profile***  
**1-** A opção para gerar o ***Log Profiler***está dentro do *SHIFT+F6,* conforme abaixo*:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26425928159511)*Selecione o diretório/ local que desejam salvar o arquivo clicando em Pesquisar.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26425928165911)Clique em iniciar e feche a aplicação na opção **sair**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26425928169111)  
  
- Execute a rotina até concluir;  
- Finalizada execução da rotina. pressione SHIFT+F6 novamente, e clique em finalizar:  
 *![](https://centraldeatendimento.totvs.com/hc/article_attachments/26425915081623)* **Atenção:***Essa opção só será efetiva se a linha **logprofiler** no **APPSERVER.INI** estiver **desabilitada  
  
Trace*** **do DbAcess****1.1-** Caso prefira, configure o ***Log Profiler*** através do seu ***APPSERVER.INI,***conforme link abaixo:  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046967894>

**2-** Para gerar o ***Trace*** do *DBaccess será* necessário efetuar os procedimentos abaixo:  
**2.1**- No *DBMonitor* acessar "Aba" Usuários.  
**2.2**- Pedir ao usuário que entre no sistema.  
**2.3**- Clicar no usuário desejado  
**2.4**- Clicar no botão inferior (Rastrear/*Trace*).  
**2.5**- Pedir ao usuário que execute o procedimento desejado.  
**2.6**- Salvar o (Rastrear/*Trace*).
