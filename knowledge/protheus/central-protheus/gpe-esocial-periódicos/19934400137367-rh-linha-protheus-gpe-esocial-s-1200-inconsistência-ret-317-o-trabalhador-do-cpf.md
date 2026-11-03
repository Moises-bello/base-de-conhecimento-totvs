---
article_id: 19934400137367
category: GPE - eSocial - Periódicos
content_hash: 12cb00b5e74db5537652a9be6653a441aa68ebbb79f9ef00ce8b81285ddc9c69
fetched_at: '2026-06-28T22:45:08.666450+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - Inconsistência RET 317 - O trabalhador
  do CPF 'x', matricula 'x', devera encontrar-se ativo no período 'x'.
type: support-article
updated_at: '2025-07-22T14:05:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19934400137367-RH-Linha-Protheus-GPE-eSocial-S-1200-Inconsist%C3%AAncia-RET-317-O-trabalhador-do-CPF-x-matricula-x-devera-encontrar-se-ativo-no-per%C3%ADodo-x
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19934428257943) Tempo aproximado para leitura: **00:02:00min****Ocorrência**Sequência: 000001 Tipo: Erro - Código da ocorrência: 317  
Descrição: O trabalhador do CPF 'x', matricula 'x', devera encontrar-se ativo no período 'x'  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa**A inconsistência 317 é retornada quando ocorre a tentativa do envio do evento S-1200 com data anterior a data da troca do CPF com o registro atualizado, ou seja, reprocessar um S-1200 de 05/2023, porém houve a troca de CPF em 06/2023.  
  
**Solução**Realize a alteração do **Tipo de Admissão** para **1 - Admissão** no S-2200/S-2300 diretamente no TAF.  
Caminho: SIGATAF > Atualizações > Eventos eSocial > Trabalhador > Cadastro Trabalhador:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19994877425303)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19994877432087)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19994856893463)  
  
Após alteração, realize a transmissão do evento S-2200/S-2300. E com retorno com sucesso da transmissão, realize novamente a tentativa de transmissão do S-1200.

**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[RH - Linha Protheus - GPE - eSocial - Troca de CPF Cadastro do Trabalhador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037231954-RH-Linha-Protheus-GPE-eSocial-Troca-de-CPF-Cadastro-do-Trabalhador)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "**Eventos**".*
