---
article_id: 19822698983831
category: GPE - eSocial - Periódicos
content_hash: d5e2b50e1eaab2df4bc94e5d76eb6f7b451bde4b6089fac16f824ab99ad0f065
fetched_at: '2026-06-28T22:45:08.987459+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1210 - Inconsistência retornada pelo
  RET: Codigo da ocorrência: 186 Localização: /eSocial/evtPgtos/ideBenef/infolRComplem/planSaude[2]/infoDepSau/cpfDep'
type: support-article
updated_at: '2023-12-13T22:04:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19822698983831-RH-Linha-Protheus-GPE-eSocial-S-1210-Inconsist%C3%AAncia-retornada-pelo-RET-Codigo-da-ocorr%C3%AAncia-186-Localiza%C3%A7%C3%A3o-eSocial-evtPgtos-ideBenef-infolRComplem-planSaude-2-infoDepSau-cpfDep
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19822658054807) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Sequência: 000001 - Tipo: Erro - Codigo da ocorrência: 186  
Localização: /eSocial/evtPgtos/ideBenef/infoIRComplem/planSaude[1]/infoDepSau/vlrSaudeDep  
Descrição: Quando o campo de Valor da deducao do rendimento tributavel do plano de saude do dependente for igual a zero, o campo Valor relativo a deducao do rendimento tributavel correspondente a pagamento a plano de saude do Titular deve ser maior que zero.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão P12.12210  
  
**Causa**  
A partir do leiaute S-1.2 é obrigatório envio das informações do Plano de saúde coletivo **quando houver desconto para o Titular ou Dependente**, porém se não houver desconto, não deve integrar tais informações e valor zerado na tag vlrSaudeTit e vlrSaudeDep.

Segue validação do eSocial:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19822701542423) Fonte: <https://www.gov.br/esocial/pt-br/documentacao-tecnica/nde-01-2023-rev-em-11-07-2023/index.html/index.html#evtPgtos>  
  
**Solução**Se o S-1210 gerar com valores zerados para Titular e Dependentes, abra um ticket e solicite a correção da issue DRHROTPRT-13751  
  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
