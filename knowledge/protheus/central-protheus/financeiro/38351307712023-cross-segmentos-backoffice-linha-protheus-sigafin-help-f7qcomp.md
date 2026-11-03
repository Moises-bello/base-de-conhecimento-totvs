---
article_id: 38351307712023
category: Financeiro
content_hash: d924ea42d9c27723ea6ec9a36f9cbd98636f49c18d6420fd8fa68691d80b1d1b
fetched_at: '2026-06-28T22:38:00.987177+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - HELP: F7QCOMP'
type: support-article
updated_at: '2026-02-12T18:30:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38351307712023-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-HELP-F7QCOMP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38351307698327) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Ao utilizar o sistema, é apresentado o help: F7QCOMP. Problema: Inconsistência no dicionário de dados. O que deve ser feito para corrigir este incidente?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38351307698967)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Versão 12.1.2210.  
  
**Solução**  
O erro **F7QCOMP** ocorre devido à ausência ou inconsistência na configuração de compartilhamento da tabela **F7Q**. Esta tabela foi implementada no dicionário de dados em decorrência das atualizações da **Reforma Tributária**.

Para solucionar o incidente, é necessário que o compartilhamento da tabela **F7Q** esteja configurado de forma idêntica ao compartilhamento da tabela **FK7** (Tabela de Movimentos Bancários).

1. Acesse o módulo **Configurador (SIGACFG)**;
2. Vá em **Dicionário de Dados** > **Base de Dados** > **Dicionário** > **Arquivos**;
3. Pesquise pela tabela **FK7** e anote o seu modo de compartilhamento. No exemplo a seguir: está totalmente exclusiva para Filial, Unidade de Negócio e Empresa, será necessário manter o mesmo compartilhamento para a **F7Q.**

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38351307699607)
4. Pesquise pela tabela **F7Q**;
5. Clique em **Editar** e ajuste os campos de compartilhamento para que fiquem exatamente iguais aos da tabela **FK7**;
6. Confirme a alteração e clique em **Salvar**;
7. Clique no ícone do **Disquete (Atualizar Base de Dados)** para confirmar a alteração no banco de dados;
8. Reinicie o Protheus e realize o teste novamente.
