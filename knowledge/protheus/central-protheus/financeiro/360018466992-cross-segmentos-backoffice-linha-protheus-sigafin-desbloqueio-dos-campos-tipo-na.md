---
article_id: 360018466992
category: Financeiro
content_hash: 8d27e4ef93d384c8b27247a1b5b12400512f56b4d52f3ee2d5b7df13476f93ea
fetched_at: '2026-06-28T22:38:02.905761+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Desbloqueio dos campos
  Tipo Natureza (ED_TIPO) e Codigo Pai (ED_PAI), no Cadastro de Naturezas
type: support-article
updated_at: '2022-06-20T22:43:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018466992-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Desbloqueio-dos-campos-Tipo-Natureza-ED-TIPO-e-Codigo-Pai-ED-PAI-no-Cadastro-de-Naturezas
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:00 min****Dúvida**  
Como habilitar os campos **Tipo Naturez** (**ED\_TIPO**) e **Código Pai** (**ED\_PAI**), no Cadastro de naturezas.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**  
Para habilitar os campos **Tipo Naturez** (**ED\_TIPO**) e **Codigo Pai** (**ED\_PAI**) é necessário configurar o parâmetro **MV\_NATSINT = 1.**

MV\_NATSINT (Indica utilização de estrutura de natureza Sintética/Analitica no cadastro de Naturezas  (Financeiro).  Opções: 1 = Sim ou 2 = Não (padrão) **Procedimento:**No configurador, acesse: Base de Dados> Dicionário> Base de Dados> Parâmetros, clique em Pesquisar (lupa), digite o parâmetro, clique em Buscar: 1. Localize o parâmetro **MV\_NATSINT** e altere o mesmo para  1 (SIM);  
2. Após a ativação deste parâmetro, o campo **ED\_PAI** e **ED\_TIPO** no cadastro da natureza estarão habilitados para uso.  
  
**Saiba mais:**  
[Naturezas - FINA010 - Financeiro - P12](http://tdn.totvs.com/display/public/PROT/Naturezas+-+FINA010+-+Financeiro+-+P12)  
[Configuração para o uso dos relatórios FINR158, FINR138 e FINR198](http://tdn.totvs.com/display/public/PROT/FIN0008_CREL_Configuracao_para_uso_dos_relatorios_FINR158_FINR138_e_FINR198)
