---
article_id: 40412285272599
category: REQUISIÇÕES
content_hash: 44162d40d7d68294ed4172c126eb87997b0befa9435414cde172384194ea9675
fetched_at: '2026-06-28T22:44:37.505466+00:00'
product: protheus
section_id: 10299632459799
source: central-protheus
title: RH - Linha Protheus - Meu RH - Como desabilitar a integração de atestados entre
  Meu RH e Quirons, mesmo tendo pelo Protheus
type: support-article
updated_at: '2026-05-12T16:39:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40412285272599-RH-Linha-Protheus-Meu-RH-Como-desabilitar-a-integra%C3%A7%C3%A3o-de-atestados-entre-Meu-RH-e-Quirons-mesmo-tendo-pelo-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40412285250455) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Ao atualizar para a última versão com o parâmetro de integração marcado, o sistema considera o lançamento do atestado integrado com o Quirons. Como desabilitar essa funcionalidade mantendo a integração ativa apenas para relatórios (ASO, NR'S), sem afetar o controle de atestados pelo RH?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
Inicialmente, a configuração dos parâmetros gerais precisa estar completa, para acessá-la clique no artigo abaixo:  
[Documentação técnica da integração](https://tdn.totvs.com/pages/viewpage.action?pageId=991880224&utm_source=chatgpt.com)  
  
Foi criado o parâmetro **MV\_MRHNG** para controlar especificamente o envio de atestados do Meu RH para o Quirons. Este parâmetro trabalha em conjunto com o **MV\_RHNG** (integração geral Protheus x Quirons).  
  
A partir da *release* **12.1.2610**, o parâmetro está disponível nativamente.   
Para versões anteriores, deve ser criado manualmente no configurador (SIGACFG).  
  
Abaixo, o comportamento do sistema conforme a configuração dos parâmetros:

* **MV\_RHNG = .T. e MV\_MRHNG = .T.**: Integração habilitada. Todo atestado lançado no Meu RH será integrado com o Quirons.
* **MV\_RHNG = .T. e MV\_MRHNG = .F.**: Integração habilitada no Protheus (para relatórios), mas desabilitada para o Meu RH. O atestado não será enviado ao Quirons e a aprovação seguirá o fluxo padrão no Protheus.
* **MV\_RHNG = .F.**: Independente do conteúdo do MV\_MRHNG, a integração está desabilitada na origem.

**Passos**  
Para criar ou configurar o parâmetro, acesse o módulo **Configurador (SIGACFG)** e siga as instruções:

1. Acesse **Ambiente > Cadastros > Parâmetros**.
2. Clique em **Incluir** (ou pesquisar caso já exista).
3. Preencha os campos conforme abaixo:

   * **Nome da Variável (X6\_VAR):** MV\_MRHNG
   * **Tipo (X6\_TIPO):** Lógico
   * **Descrição (X6\_DESCRIC):** Habilita a integração dos atestados médicos do Meu RH com o Quirons, onde .T. habilita e .F. desabilita.
   * **Valor Padrão (X6\_CONTEUD):** .T.
4. Para atender ao cenário onde o RH controla os atestados e não deve integrar com o Quirons pelo Meu RH, altere o valor para **.F.**.
5. Clique em **Confirmar** para salvar.

**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
