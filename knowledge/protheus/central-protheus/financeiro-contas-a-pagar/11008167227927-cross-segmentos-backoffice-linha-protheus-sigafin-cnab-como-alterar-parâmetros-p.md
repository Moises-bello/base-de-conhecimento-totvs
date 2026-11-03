---
article_id: 11008167227927
category: Financeiro - Contas a Pagar
content_hash: e94a9ee23f5770634687eb85669c5b663a23b35b5e0ff35b200e302ecfa649be
fetched_at: '2026-06-28T22:38:07.058509+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB - Como alterar
  parâmetros para buscar ou informar pasta de geração ou retorno
type: support-article
updated_at: '2025-08-04T19:49:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11008167227927-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-Como-alterar-par%C3%A2metros-para-buscar-ou-informar-pasta-de-gera%C3%A7%C3%A3o-ou-retorno
---

**Dúvida**Como configurar o grupo de perguntas das rotinas de CNAB para permitir a localização do arquivo via explore?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as Versões  
  
**Solução**Por padrão, a pergunta do processo permanece habilitada para que o caminho e o diretório sejam informados manualmente. No entanto, é possível personalizar essa configuração por meio do Configurador. É provável ter sido feita alguma alteração nas perguntas do seu grupo de CNAB a Receber/Pagar, o que pode estar impactando o comportamento atual.

**Para ajustar a configuração, recomendamos definir a opção da pergunta como "Buscar Arquivo", conforme demonstrado na imagem — aplicável aos campos "Arq. Configuração" e "Arq. de Saída".**

Essa alteração pode ser feita no **Configurador**, acessando o seguinte caminho:  
**Base de Dados > Dicionário > Base de Dados > Perguntas.**

**Exemplo prático:**  
Na rotina desejada, localize o campo correspondente dentro da aba **Perguntas**. Em seguida, selecione a linha e pressione **F1** no teclado. Será exibido o **Grupo de Perguntas** e o **Sequencial** correspondente.

**Exemplo:**  
Rotina **FINA420** → Campo: **Arquivo de Saída**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33940443646743)  
  
Em seguida, acesse o caminho no Configurador: **Base de Dados > Dicionário de Dados > Perguntas**, e localize o respectivo Grupo de Perguntas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33940443648663)

Clique em Editar, localize o sequencial desejado e, no campo objeto, dê um duplo clique para alterar o tipo para **FILE**. Em seguida, adicione as opções **Servidor** e **Local**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33940414249751)  
  
Após a aplicação da configuração, serão exibidas a pasta ***Protheus\_data*** do ambiente Protheus e as unidades de rede disponíveis na máquina local do usuário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33940414252055)

Perguntes relacionados

AFI150 - Arquivo de Cobranças (FINA150)  
AFI200 - Retorno de Cobranças (FINA200)  
AFI420 - Arquivo de Pagamentos (FINA420)  
AFI430 - Retorno de Pagamentos (FINA430)  
FIN680 - Extratos Bancários (FINR680)  
FIN650 - Relatório de Retorno CNAB (FINR650)  
  
**Ressaltamos que qualquer alteração deve ser realizada, preferencialmente, em ambiente de homologação antes de ser aplicada em produção.**
