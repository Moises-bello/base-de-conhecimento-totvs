---
article_id: 15946387556887
category: 'RH - Verbas '
content_hash: 068350e1261dd87a3ac16ab04d2877e0c3b3d0484c4c5d378d9243b460be3360
fetched_at: '2026-06-28T22:43:19.866974+00:00'
product: protheus
section_id: 360010838314
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ajuste no cadastro de verbas, Sistema emite alerta
  Help: NOTAB Problema: => Chave não localizada no arquivo de tabelas. Solução: Cadastre
  a tabela'
type: support-article
updated_at: '2026-04-29T14:52:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15946387556887-RH-Linha-Protheus-GPE-Ajuste-no-cadastro-de-verbas-Sistema-emite-alerta-Help-NOTAB-Problema-Chave-n%C3%A3o-localizada-no-arquivo-de-tabelas-Solu%C3%A7%C3%A3o-Cadastre-a-tabela
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15946419131031) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Ao realizar ajuste no campo **Cd. Inc. IRRF** no cadastro de verbas, sistema emite alerta:  
**Help: NOTAB** **Problema**: => Chave não localizada no arquivo de tabelas. **Solução**: Cadastre a tabela.  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/34778010617879)**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**  
Esta mensagem é apresentada em tela devido a inconsistência no **X3\_WHEN** do campo **RV\_HOMOLOG** ou na estrutura e composição de dados da tabelas **RCC - Manutenção de Tabelas.**  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

**1.** Acesso o módulo configurador (SIGACFG) e verifique se o campo **RV\_HOMOLOG** está com o **modo de edição (X3\_WHEN)** preenchido, se sim, **deixe o conteúdo em branco.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40100129778071)

**2.** Verifique se o campo **RV\_INCIRF** está com a configuração padrão.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40100174855063)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40100174856343)

**3.** Confira se as tabelas RCB e RCC estão com o mesmo compartilhamento.

**Após ajuste, realize um novo teste.**

Caso o problema persista, realize os passos abaixo:

1. Acesse rotina de **Manutenção de Tabelas** através do menu **Atualizações > Definições de Cálculo > Manutenção de Tabelas.**  
  
2. Localize a tabela **S138**, vá em **Outras Ações > Alterar.**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/34778010623383)**  
  
3. Atualize a tabela em **Outras Ações > Atualizar tabela**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34778010626839)  
  
4. Selecione **Sim** para a mensagem gerada:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34778010628247)  
  
Confirmação da atualização:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34778058240663)

**Saiba Mais**  
[RH - Linha Protheus - GPE - Pontos de Entrada da rotina GPEA040 - Cadastro de Verbas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057640854-RH-Linha-Protheus-GPE-Pontos-de-Entrada-da-rotina-GPEA040-Cadastro-de-Verbas?source=search)  
[RH - Linha Protheus - GPE - Como cadastrar verbas no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411677253783-RH-Linha-Protheus-GPE-Como-cadastrar-verbas-no-Protheus?source=search)
