---
article_id: 23945644752279
category: Financeiro - Conciliador Backoffice
content_hash: b55d937221c2f71ba586d0833db09f87262df3704a195f48da468b5f1b6effa3
fetched_at: '2026-06-28T22:37:47.143704+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 -  Conciliador
  Backoffice Financeiro
type: support-article
updated_at: '2026-01-16T11:50:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23945644752279-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Conciliador-Backoffice-Financeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23945628474775) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Após a descontinuação das rotinas de conciliação, como implantar o novo conciliador? Existem vídeos de apoio para configurar e usar a rotina **CTBA940?**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release  12.1.33.  
  
**Solução:**

Os fontes **FINA380** e **FINA473** já foram descontinuados para uso a partir de **01/01/2025.**  
Conforme divulgado nos comunicados contínuos dos últimos anos, e seguindo a evolução do Ciclo de Vida, as rotinas de Conciliadores Bancários — **Manual (FINA380)** e **Automático (FINA473)** — tiveram seu uso **bloqueado em 31/12/2024 não sendo permitido o uso a partir desta data, nem mesmo por ponto de entrada.**  
   
A rotina sucessora é o **Novo Conciliador Financeiro (CTBA940)**, disponível e funcional desde **01/2024**.  
Essa nova solução foi desenvolvida para trazer mais eficiência, modernidade e aderência ao processo de conciliação financeira.

Para iniciar a implementação, temos algumas orientações sobre o procedimento e as documentações necessárias.

Principais documentações sobre a nova rotina:

1. [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Como implantar o Conciliador Backoffice](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29104885594263-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Como-atualizar-o-Conciliador-Backoffice)
2. [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Os menus do Conciliador Backoffice não estão sendo exibidos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35032695025815-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Os-menus-do-Conciliador-Backoffice-n%C3%A3o-est%C3%A3o-sendo-exibidos)
3. [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - WIZARD de configuração do Novo Conciliador Backoffice](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29106222860567-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-WIZARD-de-configura%C3%A7%C3%A3o-do-Novo-Conciliador-Backoffice)
4. [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Conciliações do legado (FINA380 e FINA473) x CTBA940 - Conciliador BackOffice](https://centraldeatendimento.totvs.com/hc/pt-br/articles/26410683544215-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Concilia%C3%A7%C3%B5es-do-legado-FINA380-e-FINA473-x-CTBA940-Conciliador-BackOffice)
5. [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Como é mostrado os saldos no novo conciliador financeiro na opção processo 0024](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28647651562519-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Como-%C3%A9-mostrado-o-saldos-no-novo-conciliador-financeiro-na-op%C3%A7%C3%A3o-processo-0024)
6. [Cross Segmentos - Backoffice Linha Protheus - CTBA940 - Conciliação Automática no novo Conciliador Backoffice](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28116821508759-Cross-Segmentos-Backoffice-Linha-Protheus-CTBA940-Concilia%C3%A7%C3%A3o-Autom%C3%A1tica-no-novo-Conciliador-Backoffice)
7. [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Conciliação é removida após atualização de filtro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36224129533463-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Concilia%C3%A7%C3%A3o-%C3%A9-removida-ap%C3%B3s-atualiza%C3%A7%C3%A3o-de-filtro)
8. [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Conciliação Automática: Bloqueio de Match entre Registros com Valores Divergentes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35832257052567-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Concilia%C3%A7%C3%A3o-Autom%C3%A1tica-Bloqueio-de-Match-entre-Registros-com-Valores-Divergentes)
9. [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Como ajustar resolução da tela?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28117873777431-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Como-ajustar-resolu%C3%A7%C3%A3o-da-tela)
10. [Cross Segmentos - Backoffice Linha Protheus - CTBA940 - Como desconciliar o que foi conciliado pela antiga rotina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28949343147031-Cross-Segmentos-Backoffice-Linha-Protheus-CTBA940-Como-desconciliar-o-que-foi-conciliado-pela-antiga-rotina)
11. [Cross Segmentos - Backoffice Linha Protheus - CTBA940 - Cancelar Conciliação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28945869513879-Cross-Segmentos-Backoffice-Linha-Protheus-CTBA940-Cancelar-Concilia%C3%A7%C3%A3o#:~:text=Para%20cancelar%20a%20concilia%C3%A7%C3%A3o%2C%20basta,ent%C3%A3o%20clicar%20em%20Validar%2FExcluir.)
12. [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Como alterar data da movimentação bancária](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28956912629911-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Como-alterar-data-da-movimenta%C3%A7%C3%A3o-banc%C3%A1ria)
13. [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Registros conciliados não aparecem no novo conciliador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29116569437719-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Os-registros-conciliados-na-rotina-anterior-aparecem-na-rotina-CTBA940-como-n%C3%A3o-conciliados)
14. [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940- Campos FK5\_MSUIDT e IG\_MSUIDT não são preenchidos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28930423763351-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Campos-FK5-MSUIDT-e-IG-MSUIDT-n%C3%A3o-s%C3%A3o-preenchidos)
15. [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Amarrações CTBA940](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35831901591703-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Amarra%C3%A7%C3%B5es-CTBA940)
16. [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Botão para visualizar saldos da conciliação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29034582077847-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Bot%C3%A3o-para-visualizar-saldos-da-concilia%C3%A7%C3%A3o)
17. [Cross Segmentos - Backoffice Linha Protheus - CTBA940 - Conciliação Automática adicionar tarifa bancaria](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29119319340311-Cross-Segmentos-Backoffice-Linha-Protheus-CTBA940-Concilia%C3%A7%C3%A3o-Autom%C3%A1tica-adicionar-tarifa-bancaria)
18. [Cross Segmentos - Backoffice Linha Protheus - CTBA940 - Não aparece RA, PA e NCC na nova Conciliação Backoffice](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29123914080279-Cross-Segmentos-Backoffice-Linha-Protheus-CTBA940-N%C3%A3o-aparece-RA-PA-e-NCC-na-nova-Concilia%C3%A7%C3%A3o-Backoffice)
19. [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Os registros conciliados na rotina anterior, aparecem na rotina CTBA940, como não conciliado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29116569437719-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Os-registros-conciliados-na-rotina-anterior-aparecem-na-rotina-CTBA940-como-n%C3%A3o-conciliados)
20. [Cross Segmentos - Backoffice Linha Protheus - CTBA940 - Conciliação Manual no novo Conciliador Backoffice](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28113459370903-Cross-Segmentos-Backoffice-Linha-Protheus-CTBA940-Concilia%C3%A7%C3%A3o-Manual-no-novo-Conciliador-Backoffice)
21. [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Como visualizar todas as filiais no novo Conciliador Backoffice](Cross%20Segmentos%20-%20Backoffice%20Linha%20Protheus%20-%20SIGAFIN%20-%20CTBA940%20-%20Como%20visualiuzar%20todas%20as%20filiais%20no%20novo%20Conciliador%20Backoffice)
22. [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - É possível contabilizar os processos 0023 e 0024](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29207357998103-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-%C3%89-poss%C3%ADvel-contabilizar-os-processos-0023-e-0024)
23. [Cross Segmentos - TOTVS BackOffice (Linha Protheus) - Financeiro - CTBA940 - Como é construído o saldo bancário no Novo Conciliador BackOffice](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29286955140247-Cross-Segmentos-TOTVS-BackOffice-Linha-Protheus-Financeiro-CTBA940-Como-%C3%A9-construido-o-saldo-bancario-no-Novo-Conciliador-BackOffice)
24. [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Conceito de seleção de filiais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27905017906967-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Conceito-de-sele%C3%A7%C3%A3o-de-filiais)
25. [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Não consta o título no conciliador. O que validar?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30760627788183-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-N%C3%A3o-consta-o-titulo-no-conciliador-O-que-validar)
26. [Cross Segmentos - Backoffice Linha Protheus - Financeiro - CTBA940 - Conciliador não demonstra baixas via API](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37153645709591-Cross-Segmentos-Backoffice-Linha-Protheus-Financeiro-CTBA940-Conciliador-n%C3%A3o-demonstra-baixas-via-API)
27. [Cross Segmentos - Backoffice Linha Protheus - FINA050/CTBA940 - HELP EXCPARECONC ao excluir o PA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32549742573335-Cross-Segmentos-Backoffice-Linha-Protheus-FINA050-HELP-EXCPARECONC-ao-excluir-o-PA)
28. [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Não é possível a utilização desta configuração de conciliação porque não foram encontrados os seguintes campos de identificação única em seu ambiente: IG\_MSUIDT; FK5\_MSUIDT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27500826935959-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-N%C3%A3o-%C3%A9-poss%C3%ADvel-a-utiliza%C3%A7%C3%A3o-desta-configura%C3%A7%C3%A3o-de-concilia%C3%A7%C3%A3o-porque-n%C3%A3o-foram-encontrados-os-seguintes-campos-de-identifica%C3%A7%C3%A3o-%C3%BAnica-em-seu-ambiente-IG-MSUIDT-FK5-MSUIDT)
29. [Cross Segmento - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Campo Beneficiário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35519961717911-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Campo-Benefici%C3%A1rio)
30. [Cross Segmentos - Backoffice Linha Protheus - CTBA940 - Como realizar a conciliação em massa de todos os registros no novo conciliador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33666455191959-Cross-Segmentos-Backoffice-Linha-Protheus-CTBA940-Como-realizar-a-concilia%C3%A7%C3%A3o-em-massa-de-todos-os-registros-no-novo-conciliador)
31. [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Conciliador Backoffice Financeiro - Ao "Aplicar Conciliação" registros na aba "Dados da Conciliação" não marcando os campos E5\_RECONC=X , FK5\_DTDISP=AAAMMDD ou registros não indo para aba "](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34262520344983-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Conciliador-Backoffice-Financeiro-Ao-Aplicar-Concilia%C3%A7%C3%A3o-registros-na-aba-Dados-da-Concilia%C3%A7%C3%A3o-n%C3%A3o-marcando-os-campos-E5-RECONC-X-FK5-DTDISP-AAAMMDD-ou-registros-n%C3%A3o-indo-para-aba)
32. [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Exclusão de baixa / movimentação bancária aparecendo no conciliador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34192204101527-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Exclus%C3%A3o-de-baixa-movimenta%C3%A7%C3%A3o-banc%C3%A1ria-aparecendo-no-conciliador)
33. [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Conciliação por carteira](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35677234348695-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Concilia%C3%A7%C3%A3o-por-carteira)
34. [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Conciliador Backoffice: Filiais não aparecem para seleção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35863244717591-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Conciliador-Backoffice-Filiais-n%C3%A3o-aparecem-para-sele%C3%A7%C3%A3o)

**How To Disponíveis:**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Novo Conciliador Backoffice - How to](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30759888181015-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Novo-Conciliador-Backoffice-How-to)

**Saiba mais:**  
[Conciliação de Movimentos Bancários utilizando o Conciliador BackOffice](https://tdn.totvs.com/pages/releaseview.action?pageId=721003068)

[Cross Segmento - Backoffice linha Protheus - SIGAFIN - CTBA940- Novo Conciliador Bancário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22896337613463-Cross-Segmento-Backoffice-linha-Protheus-SIGAFIN-CTBA940-Novo-Conciliador-Banc%C3%A1rio?source=search)

[Processo de Conciliação de Movimentos Bancários utilizando o Conciliador BackOffice](https://tdn.totvs.com.br/pages/releaseview.action?pageId=721003068)

[Reestruturação Financeiro - Baixas e Movimento Bancário](https://tdn.totvs.com.br/pages/releaseview.action?pageId=181965434)

[Rdmake para correção de MSUIDT no estorno da baixa em lote](https://tdn.totvs.com/pages/releaseview.action?pageId=954094803)
