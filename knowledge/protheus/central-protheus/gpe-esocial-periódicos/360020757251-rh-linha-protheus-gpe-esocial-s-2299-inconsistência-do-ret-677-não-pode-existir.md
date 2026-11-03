---
article_id: 360020757251
category: GPE - eSocial - Periódicos
content_hash: d2c7f508d30b7e1a29f8bc45256b8fb574a2169519676bea18e6ca1ceaaf0bea
fetched_at: '2026-06-28T22:45:09.133448+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2299 - Inconsistência do RET - 677
  - Não pode existir qualquer evento para o vinculo trabalhista com data posterior
  a data do desligamento.
type: support-article
updated_at: '2025-07-22T14:17:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020757251-RH-Linha-Protheus-GPE-eSocial-S-2299-Inconsist%C3%AAncia-do-RET-677-N%C3%A3o-pode-existir-qualquer-evento-para-o-vinculo-trabalhista-com-data-posterior-a-data-do-desligamento
---

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27633299925527)**Tempo aproximado para leitura: **05:00 min**

**Ocorrência**Inconsistência do RET - 677 - Não pode existir qualquer evento para o vinculo trabalhista com data posterior a data do desligamento.  
  
Ação Sugerida: Não deve existir qualquer evento trabalhista para o vinculo indicado no evento de desligamento com data posterior a Data de Desligamento, data final da Quarentena ou Data Projetada para o termino do Aviso Prévio indenizado, quando houver; Não deve existir qualquer evento periódico com período de apuração que compreenda ou seja posterior ao mês do desligamento. A exceção a essa regra se restringe aos seguintes eventos: Monitoração de Saúde, Pagamento, Reintegração, Remuneração (em algumas situações especificas),e Alteração Contratual (quando data de efeito for igual ou anterior a Data de Desligamento, Quarentena ou Aviso Prévio indenizado).</descricao>  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**

**1.** O erro reportado normalmente ocorre quando há um evento **S-2205 (Alteração Cadastral do Trabalhador)** ou **S-2206 (Alteração Contratual do Trabalhador)** com data de alteração/evento posterior à data de desligamento do funcionário.  
**2.** Também há situações em que ele ocorre quando é necessário enviar um evento S-2299 - Desligamento com data retroativa, por exemplo por motivo determinação judicial.  
**3.** O erro pode ocorrer também quando há um evento S-2240 (Condições Ambientais do Trabalho - Agentes Nocivos) da medicina do trabalho com data de alteração/evento posterior a data de desligamento do funcionário.  
  
**Solução** **Para solucionar o item 1.** verifique no Portal do eSocial se houve alteração cadastral (**S-2205**) ou alteração de contratual (**S-2206**) com data posterior a data de demissão do trabalhador. Caso afirmativo, deverá ser enviado um **S-3000** (exclusão) deste registro e enviar novamente o evento S-2205 ou S-2206 com uma data de alteração inferior a data de desligamento.  
Após esse ajuste o S-2299 pode ser transmitido ao governo.  
  
**Para solucionar o item 2** é necessário reabrir o período no eSocial do qual a data de desligamento retroage com um evento S-1298 e o preencher os campos **Processo Trabalhista** e **Data Fim Quarentena** (período em que o funcionário ficou aguardando o processo trabalhista) conforme print abaixo no evento S-2299:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040724113)  
 **Para solucionar o item 3.** verifique no Portal do eSocial se houve condições ambientais do trabalho (**S-2240**) com data posterior a data de demissão do trabalhador. Caso afirmativo, deverá ser enviado um **S-3000** (exclusão) deste registro e enviar novamente o evento S-2200 com uma data de alteração inferior a data de desligamento.  
**Observação**: Se a empresa de medicina do trabalho for terceirizada, informar o procedimento a ser realizado.  
  
Após esse ajuste o S-2299 pode ser transmitido ao governo.  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)
