---
article_id: 31766438197911
category: PMS - Integrações
content_hash: 8cfcb58f978a726aafd4385d049853848017295616bd39b94ec9bacd24bab4c6
fetched_at: '2026-06-28T22:37:16.730202+00:00'
product: protheus
section_id: 1500001550742
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Mile no gestão de projetos
  (PMS)
type: support-article
updated_at: '2025-04-30T17:37:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31766438197911-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Mile-no-gest%C3%A3o-de-projetos-PMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31766438190487) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como funciona o Mile no gestão de projetos (PMS)?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões  
  
**Solução**O Mile, no PMS, não está configurado nativamente, onde seria necessário usar a opção a configuração do Mile, "3 - Função"

Dessa maneira, é apontado User Functions na função chamada pelo Mile, para a inclusão.

Exemplo: Importação da Estrutura do Projeto (AFC) através do Canal A

Primeiramente é preciso criar uma User Function que irá receber os dados do MILE e fazer a chamada da ExecAuto, este caso da rotina PMSA201.

* UserFunctionXXX(Interface, aInfos, aLayOut, aSaidas)

Veja que a UserFunction recebe quatro parâmetros onde:

1. **Interface** - Lógico - .T. se está sendo executado com interface / .F. se está sendo executado sem interface
2. **aInfos** - Array - Vetor com informações adicionais como linha inicial e final lida, nome do arquivo etc.
3. **aLayOut** - Array - Informações das definições do layout.
4. **aSaidas** - Array - Estrutura do vetor sobre dados de saída

Estes dados terão que ser tratados dentro da UserFunction antes da chamada da ExecAuto para serem devidamente enviados ao processo automático. Neste caso seguindo as condições dos parâmetros da rotina PMSA201.

* PMSA201(nCallOpcx, aGetCpos, cNivTrf, , xAutoAFC)

Onde:

1. **nCallOpcx** - Numérico - Opção da rotina a ser executada
2. **aGetCpos** - Array - Informações da Estrutura do Projeto (AFC)
3. **cNivTrf** - Caractere - Nível da Estrutura do Projeto (AGA)
4. **xAutoAFC** - Array- Informações da Estrutura do Projeto (AFC)

Neste caso, para enviar o vetor do Canal A Master (AFC) como segundo parâmetro (aGetCpos), vamos precisar manipular o array de canais criado pelo MILE.

**Saiba mais:**

[PMS0041 Importação de Projetos via MILE](https://tdn.totvs.com/x/0aBBKw)
