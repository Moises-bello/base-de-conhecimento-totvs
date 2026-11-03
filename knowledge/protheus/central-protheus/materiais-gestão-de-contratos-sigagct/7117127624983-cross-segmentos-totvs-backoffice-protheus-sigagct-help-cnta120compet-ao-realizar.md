---
article_id: 7117127624983
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: ba2a6e2a0cc0b93ca49a441ae8c2ce811bba8927574d4b24135dabfd48029e9a
fetched_at: '2026-06-28T22:37:22.919947+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help CNTA120COMPET
  ao realizar uma medição
type: support-article
updated_at: '2026-05-20T12:09:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7117127624983-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-CNTA120COMPET-ao-realizar-uma-medi%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20411130747031) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Ao incluir uma medição ocorre o Help CNTA120COMPET ao escolher um Contrato o Competência

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11453574192919)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**  
Em ocorrências já verificadas do mesmo help CNTA120COMPET as possibilidades que podem ser verificadas são:

**1 -** Haver medição em aberto para o contrato (Medição que foi apenas incluída e não foi encerrada - Status Vermelho), necessitando assim ser encerrada ou excluída para se inserir uma nova medição.

**2 -** Falta de saldo para o contrato/planilha/competência, necessitando assim a revisão do contrato para se inserir mais saldo caso desejado.

Em relação a checagem de saldo do contrato/planilha/competência da opção 2, um teste que pode ser realizado em ambiente de homologação, é a realização do Processamento do Recalculo dos Saldos do Contrato, mencionada artigo do link abaixo, verificando se ocorre alguma alteração de valores de saldos, alteração essa que possa corrigir o problema em questão da medição do contrato em específico ou verificando a falta do saldo após o recálculo.

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar o Reajuste de Saldo em contratos, planilhas e cronograma financeiro ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020124591-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-o-Reajuste-de-Saldo-em-contratos-planilhas-e-cronograma-financeiro-?source=search)

**3 -** Falta de permissão do usuário para realizar a medição  ( [MP - SIGAGCT - Controle de Acesso ao contrato no Gestão de Contratos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016499391-MP-SIGAGCT-Controle-de-Acesso-ao-contrato-no-Gest%C3%A3o-de-Contratos?source=search) )

**4 -** Data da realização da medição fora das datas de vigencia "Inicio" e "Fim" do Contrato e/ou Data Inicio e Fim da Planilha que se está medindo.

**5 -** Uma outra possibilidade que pode ser verificada referente à mensagem é relacionada à inconsistência na base de dados, com falta de informação no campo ***CNA\_CRONOG*** (estando em branco) onde, sendo uma planilha com Cronograma  Financeiro, este campo necessita estar preenchido com o número do cronograma referente à planilha deste registro da tabela CNA.

Caso necessário, orientamos realização da análise da base junto a um analista especialista em loco que pode ser solicitado junto ao ESN Totvs que atende a empresa.

***Saiba Mais:***

[Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
