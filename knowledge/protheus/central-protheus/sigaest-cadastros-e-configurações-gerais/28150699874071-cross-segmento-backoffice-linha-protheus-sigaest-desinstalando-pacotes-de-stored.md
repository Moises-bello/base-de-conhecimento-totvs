---
article_id: 28150699874071
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 9567a777838c1a3d4493c5704273cbc80cd6954af2f8ee8add5788d16e72c4bb
fetched_at: '2026-06-28T22:39:08.193195+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Desinstalando pacotes
  de Stored Procedures
type: support-article
updated_at: '2024-12-05T19:05:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28150699874071-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Desinstalando-pacotes-de-Stored-Procedures
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28150729438615) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**Como desinstalar as novas procedures com o Novo Gestor de Stored Procedures (CFGX051M)?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todos os Módulos - Todas as versões

**Solução**

Abaixo orientamos sobre a Desinstalção dos pacotes de Stored Procedures através do Novo Gestor de Stored Procedures (CFGX051M) seguindo as premissas do documento oficial: [Stored Procedures - Novo gerenciador de pacotes](Stored%20Procedures%20-%20Novo%20gerenciador%20de%20pacotes)

Acesse também: [Stored Procedures utilizadas no produto Estoque e Custos](https://tdn.totvs.com/x/wi3AFQ)

**Nova interface**

A principal mudança na interface será a apresentação das empresas disponíveis no ambiente e todos os processos existentes para gerenciamento ao mesmo tempo, em uma mesma janela:

![](https://tdn.totvs.com/download/attachments/651665430/image2022-7-12_15-6-26.png?version=1&modificationDate=1657649186450&api=v2)

**Desinstalando pacotes de procedures**

O procedimento para desinstalação de pacotes é semelhante ao **Processo de Instalação**.

**IMPORTANTE:** Este procedimento necessita de acesso exclusivo em algumas tabelas do banco de dados e por isso não pode haver concorrência.

Para realizar a desinstalação:

* Selecionar em quais empresas os processos serão desinstalados:  
  ![](https://tdn.totvs.com/download/attachments/651665430/worddav466b0dd8c744edb398d910a1d5096981.png?version=1&modificationDate=1637355053203&api=v2)

* Selecionar quais processos serão desinstalados:  
  ![](https://tdn.totvs.com/download/attachments/651665430/worddavf76c7baf5789bc32949472a7886ca589.png?version=1&modificationDate=1637355053233&api=v2)

Após selecionar as empresas e processos, basta clicar no botão ![](https://tdn.totvs.com/download/attachments/651665430/worddavde157571e60718492642fc5ecfcdb29d.png?version=1&modificationDate=1637355052717&api=v2) (desinstalar processos).

* Será exibida uma janela com alguns avisos solicitando a confirmação da desinstalação:  
  ![](https://tdn.totvs.com/download/attachments/651665430/worddav7eff411a5f723fc230acbfc0717c7cfa.png?version=1&modificationDate=1637355053400&api=v2)

* Ao confirmar, surgirá uma outra janela exibindo o andamento da desinstalação:  
  ![](https://tdn.totvs.com/download/attachments/651665430/worddav0379bc81e46f652071c361ea714b8ecb.png?version=1&modificationDate=1637355053433&api=v2)

* Ao final do procedimento surgirá uma janela contendo o log da operação realizada:  
  ![](https://tdn.totvs.com/download/attachments/651665430/worddavc206bae9b66de38e52c9a3198bde5a03.png?version=1&modificationDate=1637355053470&api=v2)

No botão **Outras Ações** é possível gerar o relatório deste log.  
Ao fechar a janela de log, a interface principal será atualizada para refletir o status atual:  
![](https://tdn.totvs.com/download/attachments/651665430/image2022-7-12_15-43-53.png?version=1&modificationDate=1657651434430&api=v2)

Para mais informações sobre as funcionalidades acesse a documentação: [Stored Procedures - Novo gerenciador de pacotes](https://tdn.totvs.com/x/FqDXJg)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*

[Instalando pacotes de Stored Procedures](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28150721529623-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Instalando-pacotes-de-Stored-Procedures)

[Processo no antigo Gestor de Stored Procedure](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28150717052439-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Processo-no-antigo-Gestor-de-Stored-Procedure)
