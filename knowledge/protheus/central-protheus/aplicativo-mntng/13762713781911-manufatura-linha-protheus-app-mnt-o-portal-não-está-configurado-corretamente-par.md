---
article_id: 13762713781911
category: 'Aplicativo MNTNG '
content_hash: bc9f96f20cf193685e8bd18e16bf45faa19a2193771fd2f847216a5e4c82c6a9
fetched_at: '2026-06-28T22:42:37.746007+00:00'
product: protheus
section_id: 360010992174
source: central-protheus
title: Manufatura - Linha Protheus - APP MNT - O portal não está configurado Corretamente
  para autenticação
type: support-article
updated_at: '2023-04-12T12:09:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13762713781911-Manufatura-Linha-Protheus-APP-MNT-O-portal-n%C3%A3o-est%C3%A1-configurado-Corretamente-para-autentica%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao acessar o aplicativo **MNTNG** é apresentado a mensagem de **O portal não está configurado corretamente para autenticação via Mingle!**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13762071993879)

**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Aplicativo MNTNG - Todas as versões  
  
**Causa**A situação acontece porque acabou o prazo de utilização do **MNTNG via** **autenticação via licença MNT**.  
  
**Solução**A partir de **Julho de 2022** foi liberado a utilização do **MNTNG** utilizando a **autenticação via** **Mingle**, a orientação para adequação para o novo modelo de autenticação era de até **30 de Março de 2023,** visto que a partir de **abril de 2023**, o modelo de **autenticação via licença MNT foi descontinuado**. Então será necessário seguir os itens do artigo [Manufatura - Linha Protheus - APP MNT - Consumo de Licença do MNT NG via Mingle](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7052945414167) para **solicitar um Alias Mingle único**, verificar a existência das **licenças com código 3033 no servidor de licenças do ambiente. Caso não possua será necessário entrar em contato com o ESN da empresa para contratação**. E por último realizar os ajustes na **configuração do Web Service** **Rest**  para o uso da **autenticação via Mingle** de acordo com orientação do guia de [implementação do MNTNG](https://tdn.totvs.com/display/PROT/Implementando+o+Mobile+%28MNT+NG%29+-+Protheus).  
  
**Saiba mais**Para informações de regras de *firewall* no *link* [Manufatura - Linha Protheus - APP MNT - Configuração do Firewall para autenticação do Portal Mobile e WebService](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025455154)
