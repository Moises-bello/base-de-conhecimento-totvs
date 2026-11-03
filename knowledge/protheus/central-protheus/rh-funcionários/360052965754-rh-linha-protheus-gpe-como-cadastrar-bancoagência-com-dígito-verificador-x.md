---
article_id: 360052965754
category: RH - Funcionários
content_hash: 5d765e23cf404f1a98f190eabb57e2371aab72290a882ca36a649e7b4b63109c
fetched_at: '2026-06-28T22:43:27.487274+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Como cadastrar banco/agência com dígito verificador
  X
type: support-article
updated_at: '2025-09-30T01:45:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052965754-RH-Linha-Protheus-GPE-Como-cadastrar-banco-ag%C3%AAncia-com-d%C3%ADgito-verificador-X
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16638627321879) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como cadastrar banco/agência com dígito verificador X?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**  
1. Selecione o campo que será alterado epressione F1 para conferir o **nome** do campo. Neste caso trata-se do **RA\_BCDEPSA**.  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26572076138007)**2. Para ajustá-lo, acesse o ambiente **SIGACFG** (Configurador) com senha de **administrador** através do menu **Base de Dados > Dicionário > Base de Dados**.  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26572044551575)**3. Clique no **expansor** ao lado da empresa que acessou e selecione **Dicionário de Dados.** No ícone de **lupa,** busque pela tabela **SRA** e depois clique em **alterar** (ícone de folha com lápis). **![](https://centraldeatendimento.totvs.com/hc/article_attachments/26572044556695)**

4. Clique no **expansor** ao lado do nome da tabela (Funcionários) e selecione a opção campos. Busque pelo campo **RA\_BCDEPSA** noíconeda **lupa** e depois clique em **editar** (ícone de folha com lápis).  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26572044560151)**  
  
5. O **formato** do campo por padrão estará configurado **@R 999/99999.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26572044563607)  
  
6. Para que o Sistema permita a inclusão de *caracter,* alterare o**Formato** do campo para **@R 999/99999N.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26572044566935)  
  
Para salvar as alterações, clique na opção atualizar **Base de Dados** (ícone de disquete), depois em avançar e por último **finalizar.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26572044570775)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26572044577431)  
  
7. Após alteração, acesse o cadastro de funcionários , selecione o campo **RA\_BCDEPSA,** e digite a agência com dígito verificador X conforme necessidade.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26572044586135)

**Saiba Mais**[RH - Linha Protheus - GPE - Como retirar a obrigatoriedade dos campos da CTPS - RA\_NUMCP e RA\_SERCP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055301554-RH-Linha-Protheus-GPE-Como-retirar-a-obrigatoriedade-dos-campos-da-CTPS-RA-NUMCP-e-RA-SERCP?source=search)  
[RH - Linha Protheus - GPE - Como incluir o traço (-) na conta bancária no cadastro de funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7894739561239-RH-Linha-Protheus-GPE-Como-incluir-o-tra%C3%A7o-na-conta-banc%C3%A1ria-no-cadastro-de-funcion%C3%A1rio?source=search)  
[Artigos Gestão de Pessoas (SIGAGPE)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000926522-Gest%C3%A3o-de-Pessoas-SIGAGPE)  
[Artigos Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
