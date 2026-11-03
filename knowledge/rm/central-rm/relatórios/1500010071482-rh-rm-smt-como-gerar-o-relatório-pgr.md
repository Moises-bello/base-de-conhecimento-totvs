---
article_id: 1500010071482
category: Relatórios
content_hash: 7358ae44ccd459b4f58dd0f153a79ca3ba07dc4258edea5cd17246b3d876dda9
fetched_at: '2026-06-28T22:47:43.467292+00:00'
product: rm
section_id: 1500000861522
source: central-rm
title: RH - RM - SMT - Como gerar o Relatório PGR
type: support-article
updated_at: '2026-03-05T13:02:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010071482-RH-RM-SMT-Como-gerar-o-Relat%C3%B3rio-PGR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16036065181975) Tempo aproximado para leitura: 00:02:00 min**  
  
**Dúvida**  
Como gerar o relatório PGR(Programa de Gerenciamento de Risco)?    
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional  
  
**Solução**  
Para geração do relatório PGR é necessário realizar os seguintes passos:  
  
1. A estrutura do relatório fica disponível no book, que se encontra no RM | Gestão | TOTVS Compartilhamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16700495962519)

Importe o relatório RHUREL0027 - PGR., observando o banco de dados (Oracle / SQL). No link abaixo segue o documento com o passo a passo de como realizar o processo de importação:    
[TOTVS RH - Linha RM - SMT - Importação de relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409650455703-TOTVS-RH-Linha-RM-SMT-Importa%C3%A7%C3%A3o-de-relat%C3%B3rios)  
  
2. Verifique se o usuário tem acesso aos menus: **Relatórios PGR, Tipos de Relatório> Gerar modelo de PGR** para verificação acesse no modulo Serviços Globais o menu **Segurança | Perfis**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16700737989271)  
  
3. Após liberar as permissões, retorne ao modulo Segurança e Saúde Ocupacional e acesse o menu **Relatórios | Tipos de Relatórios**, inclua um novo registro marcando em 'Tipo' a opção PGR:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16700898418583)

4. Após salvar o tipo criado, acesse a opção**Anexos | Itens de Relatório** e, valide se há registros no anexo, caso tenha os exclua.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16701019660183)  
  
5. Selecione tipo criado e acesse a opção  Processos >> Gerar modelo de PGR, e ao aparecer a mensagem **'Deseja inserir automaticamente os itens de modelo para este tipo?',** clique em **sim,** Após executar o processo, clique no botão atualizar, para carregar os itens.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16701406591255)

6. Para geração do arquivo acesso o menu **Relatórios | Relatórios PGR**, inclua um novo registro, preencha os campos obrigatórios e as informações necessárias para geração do relatório.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16701553604759)

7. Após o preenchimento na guia Gerar/ Visualizar, clique na opção gerar relatório e posteriormente visualizar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16701813501975)  
  
  
**Saiba mais**  
Para mais orientações a respeito da geração correta do relatório, valide as documentações a seguir:

- [RH - RM - SMT - Cadastros necessários para gerar o relatório PGR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6298978683159-RH-RM-SMT-Cadastros-necess%C3%A1rios-para-gerar-o-relatorio-PGR)  
- [Como Fazer - RELATÓRIO PGR](https://tdn.totvs.com.br/display/public/LRM/Como+Fazer+PGR)
