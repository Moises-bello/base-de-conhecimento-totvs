---
article_id: 40206865787799
category: Contabilidade Gerencial - Entidades
content_hash: bf2e940906317c57529b07ec4358a8204d637fe020c26144a0027582c73b5abf
fetched_at: '2026-06-28T22:40:49.788154+00:00'
product: protheus
section_id: 1500001537661
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - Adequação da
  contabilidade à Resolução ANTAQ
type: support-article
updated_at: '2026-05-04T13:34:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40206865787799-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACTB-Adequa%C3%A7%C3%A3o-da-contabilidade-%C3%A0-Resolu%C3%A7%C3%A3o-ANTAQ
---

No Protheus, não há rotina específica para relacionar automaticamente o plano de contas regulatório da ANTAQ com o contábil da empresa. O controle pode ser feito via rotinas existentes para contabilidade societária e regulatória, usando visão gerencial (CTBA161) para diferentes demonstrações ou criando nova empresa/filial para outro plano de contas, com consolidação via CTBA220, CTBA231 ou CTBA290.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40206872643607) Tempo aproximado para leitura: **10 min**  
  
**Dúvida**  
Existe no Protheus alguma rotina, funcionalidade ou processo padrão que permita realizar o relacionamento (de/para) entre o plano de contas regulatório da ANTAQ e o plano de contas contábil da empresa, para atender à Resolução ANTAQ?  
  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - a partir da versão 12  
  
  
**Solução**  
Atualmente, não existe uma rotina específica para realizar o relacionamento automático com o plano de contas regulatório da ANTAQ. O Protheus não possui a possibilidade de controlar mais de um plano de contas ou qualquer outra entidade de forma simultânea e exclusiva na mesma Empresa/Filial caso o cadastro seja compartilhado.

Para atender a essa necessidade, o controle pode ser realizado através das rotinas já existentes para contabilidade societária e regulatória. O usuário precisará verificar como o gerenciamento será feito e como poderá aproveitar o plano de contas e os saldos já existentes na base de dados.

Existem duas alternativas principais recomendadas:

* **Utilização de Visão Gerencial (CTBA161):** Caso o gerenciamento necessite apenas de uma visão diferente nos demonstrativos contábeis, e os saldos sejam os mesmos que já constam nas contas, centros de custo ou entidades adicionais, pode-se utilizar a visão gerencial. Ao criar uma visão gerencial informando a codificação, a nomeação das entidades e a amarração que compõe o saldo, o usuário redefine a demonstração dos saldos em relatórios como DRE, Balanço e Balancete.   
    
  [Arquivos modelos - visões gerenciais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115008505768-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-arquivos-modelos-plano-referencial-vis%C3%B5es-gerenciais?source=search)   
  [CTBA161 -](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007545672-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-importar-Vis%C3%A3o-Gerencial?source=search)[Como importar Visão Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007545672-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-importar-Vis%C3%A3o-Gerencial?source=search)
* **Criação de Nova Empresa/Filial:** Se houver a necessidade de possuir um outro plano de contas com lançamentos específicos, o usuário poderá criar uma nova Empresa/Filial com as contas necessárias. Feito isso, deve-se utilizar as rotinas de Consolidação (CTBA220, CTBA231) ou Intercompany (CTBA290) para enviar os lançamentos e saldos das filiais necessárias para a nova empresa criada. Dessa forma, será possível extrair relatórios detalhados, como o razão contábil.   
    
  [CTBA220 - Consolidação Geral](https://tdn.totvs.com/pages/viewpage.action?pageId=233750748)  
  [CTBA231 - Consolidação configurada](https://tdn.totvs.com/pages/viewpage.action?pageId=6068450)  
  [CTBA290 - Intercompany](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015138212-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA290-Intercompany)

**Saiba mais:**  
[Contabilidade Regulatória e Societária no Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=795100831)
