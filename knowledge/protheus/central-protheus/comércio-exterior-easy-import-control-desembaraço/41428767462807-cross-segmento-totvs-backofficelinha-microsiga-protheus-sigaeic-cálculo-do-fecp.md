---
article_id: 41428767462807
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 9e936491b939de6d203cf6efac04f25273dd4fd43962e7db84fde775289bbabd
fetched_at: '2026-06-28T22:39:51.414256+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice(Linha Microsiga Protheus) - SIGAEIC - Cálculo
  do FECP no Recebimento de Importação
type: support-article
updated_at: '2026-06-24T19:43:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41428767462807-Cross-Segmento-TOTVS-Backoffice-Linha-Microsiga-Protheus-SIGAEIC-C%C3%A1lculo-do-FECP-no-Recebimento-de-Importa%C3%A7%C3%A3o
---

O sistema TOTVS Protheus permite configurar e calcular a majoração do ICMS relativa ao FECP na rotina de Recebimento de Importação para gerar Notas Fiscais. Inclui o campo "% ICMS FECP" no cadastro de CFO para destacar a alíquota do FECP. O processo envolve cadastro do CFO, ajuste do desembaraço e geração da Nota Fiscal de Importação com os valores do FECP destacados.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41428767438615) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como configurar e realizar o cálculo de majoração de ICMS relativo ao FECP (Fundo Estadual de Combate à Pobreza e às Desigualdades Sociais) na rotina de Recebimento de Importação para a geração de Notas Fiscais de Importação?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - Todas as Versões  
  
**Solução**  
O sistema disponibiliza a implementação do cálculo do FECP no ICMS na rotina de Recebimento de Importação (EICDI154) para a geração de Notas Fiscais de Importação. Para tal, foi adicionado o campo "**% ICMS FECP**" no cadastro de CFO (EICOP100) para indicar qual a alíquota da FECP que está contida na alíquota do ICMS, permitindo que o valor da FECP seja destacado na Nota Fiscal. Esta melhoria atende ao requisito legal da FECP para o estado do Rio de Janeiro, mas também pode ser aplicada a outros estados.  
  
**Sequência 001: Cadastro de C.F.O:**  
- No Easy Import Control (SIGAEIC), acesse a rotina "***Atualizações / Tabelas / CFO (EICOP100)***";  
- Clique em Incluir;  
- O sistema exibirá a opção de inclusão de C.F.O. com o campo “**% ICMS FECP” (WZ\_ALFECP);**  
**-** Preencha os dados do cadastro. Tenha em atenção que o percentual informado no campo **“Aliq.ICMS” (WZ\_AL\_ICMS)** deve compor a alíquota de "**ICMS + alíquota do FECP**". Informe no campo **“% ICMS FECP” (WZ\_ALFECP)** somente a alíquota do FECP a destacar para esta operação e clique no botão confirmar;  
- Clique no botão Salvar;  
- Verifique através dos registos de C.F.O. que o registo foi gravado com sucesso.  
  
**Sequência 002: Ajuste do Desembaraço (conforme a parametrização do parâmetro MV\_TEM\_DI):**  
- **Desembaraço sem D.I. Eletrónica (MV\_TEM\_DI = .F.) - "*****Apropriação C.F.O. / Regime de tributação / Adições"*****:**  
**-** Certifique-se de que possui um Desembaraço cadastrado;  
- No SIGAEIC, acesse a rotina "***Atualizações / Desembaraço / Apropriação CFO (EICOP110)***";  
- Informe o número do Desembaraço e clique em Salvar;  
- Em Outras Ações, clique em Alterar;  
- Informe a operação e clique em Ok;  
- Clique em Salvar;  
- Acesse à rotina "***Atualizações / Desembaraço / Manutenção (EICDI502)***";  
- Caso não existam as alíquotas dos impostos informadas na N.C.M. associada aos itens, acesse a rotina de "**Regime de Tributação**" no submenu e efetue a gravação do regime de tributação para os itens das invoices, informando as alíquotas;  
- Acesse a rotina de Adições e efetue a geração das adições do processo;  
- Informe os dados da D.I. e guarde a manutenção do processo.  
  
**Sequência 003: Geração de Nota Fiscal de Importação:**  
**-** Certifique-se de que possui um Desembaraço cadastrado com adições geradas e dados da D.I. informados;  
- No SIGAEIC, acesse a rotina "***Atualizações / Desembaraço / Receb. Importacao (EICDI154)***";  
- Selecione o registo pretendido e clique em Primeira;  
- Dentro do processo, clique em "***Itens***";  
- Verifique que os campos com os percentuais e valores da FECP apurados para cada item são exibidos;  
- Marque os itens, informe o número e série da Nota Fiscal;  
- Clique em Gera NFE;  
- Ao final do processamento, o sistema exibirá a confirmação da geração da NFE.  
  
**Nota:** *Caso o parâmetro "**MV\_EASY**" esteja ativo, a Pré-Nota originada no SIGAEIC e gerada no módulo SIGACOM terá as alíquotas e valores dos itens gravados nos itens da Nota Fiscal deste módulo (consulte a tabela SD1).*  
  
**Saiba mais:** [**3057376\_DTRADE-49\_DT\_Cálculo do FECP (Fundo Estadual de Combate à Pobreza e às Desigualdades Sociais) no ICMS**](https://tdn.totvs.com/pages/viewpage.action?pageId=267801906)
