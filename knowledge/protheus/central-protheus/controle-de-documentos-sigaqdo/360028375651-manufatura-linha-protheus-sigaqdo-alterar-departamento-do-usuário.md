---
article_id: 360028375651
category: Controle de Documentos (SIGAQDO)
content_hash: bb2bd4946ae96a75d624b2b16a79eccb6452a7b9e06205f0383be7d6d647063e
fetched_at: '2026-06-28T22:42:28.917101+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Alterar departamento do usuário
type: support-article
updated_at: '2025-02-12T18:42:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028375651-Manufatura-Linha-Protheus-SIGAQDO-Alterar-departamento-do-usu%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22512589312151)**Tempo aproximado para leitura: **00:01:15 min****Dúvida**Como alterar o departamento de um usuário para outro departamento?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**Para realizar a alteração do departamento de um usuário na rotina **QAXA010 - Responsáveis/Usuários**, é necessário verificar o conteúdo do parâmetro **MV\_QGINT - Indica se os módulos Quality estão integrados com Módulo SIGAGPE e não habilita a opção de Incluir**. Este parâmetro aceita as seguintes opções:

* **S**: indica que existe integração com o **RH - Recursos Humanos**, e neste caso, a alteração/transferência do departamento deve ser realizada pelo módulo de **Gestão de Pessoas**.
* **N**: indica que não existe integração com o **RH**, e neste caso, deve ser efetuado os passos abaixo:
  1. efetuar *login* com um usuário diferente do usuário que será transferido;
  2. acessar a rotina **QAXA010**;
  3. selecionar o usuário em questão;
  4. em **Outras Ações** selecionar a opção **Transferir Departamento**;
  5. informar o novo **departamento**;
  6. e **Confirmar**.

**Observação**Ao realizar a transferência de departamento do funcionário no **SIGAGPE** na rotina **GPEA180 - Transferências** com integração com o **QUALITY** é necessária a posterior transferência de responsabilidades para o próprio usuário na rotina **QAXA010**. Esse processo atualiza o departamento nas tabelas relacionadas ao processo de manutenção dos **documentos**, permitindo desta forma dar seguimento na baixa das pendências do usuário cujo departamento foi transferido via **SIGAGPE**. **Saiba mais**  
Artigo contendo as instruções de como efetuar transferência de pendência para usuário [Manufatura - Linha Protheus - SIGAQDO - Transferência de pendências para um novo usuário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021357911-MP-QUA-Transfer%C3%AAncia-de-pend%C3%AAncias-para-um-novo-usu%C3%A1rio)
