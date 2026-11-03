---
article_id: 14756922851223
category: GPE - eSocial - Não Periódicos
content_hash: 8f1bb201b4b286df2b9a2a5597974a445ee4e362a8d21e95b914d0c9fb575375
fetched_at: '2026-06-28T22:45:04.657823+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2205 - Inconsistencia do RET 304 -
  Não existe um Contrato de Trabalho para o CPF 'XXX' ou este encontra-se encerrado
  na data do evento
type: support-article
updated_at: '2026-06-16T11:27:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14756922851223-RH-Linha-Protheus-GPE-eSocial-S-2205-Inconsistencia-do-RET-304-N%C3%A3o-existe-um-Contrato-de-Trabalho-para-o-CPF-XXX-ou-este-encontra-se-encerrado-na-data-do-evento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24317230740887) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao tentar transmitir os eventos S-2205 - Alteração Cadastral, o governo retorna a inconsistência:

Código da Resposta: **304 - Não existe um Contrato de Trabalho para o CPF 'XXX' ou este encontra-se encerrado na data do evento**  
  
Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14759263786263)

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**Esse erro ocorre em 03 situações:

1. Está querendo enviar a alteração cadastral, mas o evento mas o S-2200 ou não foi enviado ao governo;
2. Está querendo enviar a alteração cadastral com a data anterior a data de admissão do funcionário;
3. Está enviando a alteração cadastral após a data de demissão do funcionário.

**Solução**

1. Acesse o cadastro do funcionário no TAF e veja se o registro S-2200 esta com numero de recibo informado. Caso não esteja precisa verificar se o S-2200 está inconsisteste, ajustar e enviar a admissão. Somente após o envio da admissão é possivel enviar a alteração cadastral.
2. Como o ingresso dele na empresa ainda não ocorreu o CPF dele realmente não estará vinculado a empresa, sendo assim nesse caso precisa gerar a alteração cadastral com data de alteração após a data de admissão dele.  
   **Exemplo:** Admissão em 10/05/2023, está enviando o S-2205 com data de alteração em 09/05/2023,  um dia antes da data inicial dele na empresa, logo nessa data ainda não existe um contrato de trabalho para esse trabalhador.
3. Como a rescisão dele já ocorreu esse contrato de trabalho já se encontra encerrado, não podendo assim gerar essa alteração, sendo assim precisa excluir o S-2205 que esta com inconsistencia.  
   **Exemplo:** Rescisão em 10/05/2023, e está enviando o S-2205 com data de alteração em 15/05/2023, Cinco dias após o desligamento dele na empresa.

**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
