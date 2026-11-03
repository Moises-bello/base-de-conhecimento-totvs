---
article_id: 360028876411
category: GPE - eSocial - Periódicos
content_hash: 245c79fc1550a05d6c01e96afd21df1798e034246eab9df7cefda0ea75682801
fetched_at: '2026-06-28T22:45:07.659417+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1200 - Código da Ocorrência 851: A
  exclusão de remuneração, desligamento e tsv termino não e aceita quando houver pagamento
  relacionado.'
type: support-article
updated_at: '2025-07-21T20:10:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028876411-RH-Linha-Protheus-GPE-eSocial-S-1200-C%C3%B3digo-da-Ocorr%C3%AAncia-851-A-exclus%C3%A3o-de-remunera%C3%A7%C3%A3o-desligamento-e-tsv-termino-n%C3%A3o-e-aceita-quando-houver-pagamento-relacionado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16040253158807) Tempo aproximado para leitura: **00:02:00min****Ocorrência**Sequência: 000001 - Tipo: Erro - Código da ocorrência: 851  
Descrição: A exclusão de remuneração, desligamento e tsv termino não e aceita quando houver pagamento relacionado. Ação Sugerida: Antes de excluir a remuneração ou desligamento exclua as informações de pagamento relacionadas.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
 **Causa**Essa mensagem ocorre quando enviado o evento S-3000 para excluir um S-1200 ou S-2299, mas já existe um evento **S-1210 associado** posterior a eles.  
Os eventos S-1200 e S-2299 são eventos de remuneração e são predecessores ao S-1210 que é um evento de pagamento.  
Caso seja transmitido um S-1210 sem um S-1200 ou S-2299 o RET (Governo) vai rejeitar, o mesmo ocorre se tentarmos excluí-los antes de excluir o S-1210.  
  
**Solução** **1.** Excluir o evento S-1210 com um S-3000.   
**2.** Somente após o RET (Governo) aceitar o evento S-3000 para a exclusão do S-1210 é que será possível retificar ou excluir um evento S-1200 e/ou S-2299.  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[MP - GPE - eSocial - S-3000 - Como realizar a exclusão de um Evento Periódico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027742231)[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade****WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
