---
article_id: 4409044099223
category: RH - Definições de Cálculo
content_hash: 40da53ee5e0a5bd3dd289d71f42299d973977888abfebd6925e6e82f6d9d003c
fetched_at: '2026-06-28T22:43:22.258246+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Atualização tabela S138 - Códigos de Incidência
  Tributária da Rubrica para o IRRF
type: support-article
updated_at: '2026-06-26T17:39:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409044099223-RH-Linha-Protheus-GPE-Atualiza%C3%A7%C3%A3o-tabela-S138-C%C3%B3digos-de-Incid%C3%AAncia-Tribut%C3%A1ria-da-Rubrica-para-o-IRRF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41522842331543)** Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Criação da tabela S138 Códigos de Incidência Tributária da Rubrica para o IRRF e como realizar a atualização quando necessário?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Criação de nova tabela em manutenção de tabelas para o leiaute da Simplificação do eSocial, de acordo com a Tabela 21: Códigos de Incidência Tributária da Rubrica para o IRRF do Anexo I.

Tabela **S138: Incid. Tributária Rubrica IRRF**e registros preenchidos conforme os itens da tabela 21 (vide anexo), com exibição condicionada ao leiaute S-1.0 (versão 9.0). Campos:

|  |  |
| --- | --- |
| **Código:** | 4 dígitos (Formato Caracter) |
| **Descrição:** | 160 Caracteres |
| **Início:** | Data (Formato dd/mm/aaaa) |
| **Término:** | Data (Formato dd/mm/aaaa) |
| **Grupo:** | 70 Caracteres |

Após Atualizações e alteração do leiaute para o simplificado, acesse **Definição de Tabela** e clique em **visualizar na tabela S138.**  
Acesse agora **Manutenção de Tabelas,** selecione a **tabela S138** e clique **Alterar.**  
Quando abrir a tabela, clique em **Outras Ações > Atualizar.**  
**![smartclient_4sf2TD1cYv.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/25071743485335)**  
  
Para que a tabela seja apresentada corretamente, deve ser verificado o conteúdo do parâmetro **MV\_VLESOC** e também estar com as atualizações de finte e dicionário do link a seguir:  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)

**Saiba Mais**  
[O trabalhador possui cálculo com dedução simplificada de IR, mas não há verba com a incidência IR 68](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25916789634839-RH-Linha-Protheus-GPE-eSocial-Eventos-Peri%C3%B3dicos-O-trabalhador-possui-c%C3%A1lculo-com-dedu%C3%A7%C3%A3o-simplificada-de-IR-mas-n%C3%A3o-h%C3%A1-verba-com-a-incid%C3%AAncia-IR-68)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)
