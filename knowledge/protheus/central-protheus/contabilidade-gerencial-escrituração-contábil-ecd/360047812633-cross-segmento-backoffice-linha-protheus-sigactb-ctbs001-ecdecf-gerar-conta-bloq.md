---
article_id: 360047812633
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: d298e2db9fba83327ab235a5e66352afe92ee6b13e625f4fab221f5f6eb8a3b1
fetched_at: '2026-06-28T22:40:44.419478+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 : ECD/ECF GERAR
  CONTA BLOQUEADA , SEM SALDO ANTERIOR E OU SEM MOVIMENTO NO PERIODO'
type: support-article
updated_at: '2022-05-03T13:27:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047812633-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-ECF-GERAR-CONTA-BLOQUEADA-SEM-SALDO-ANTERIOR-E-OU-SEM-MOVIMENTO-NO-PERIODO
---

**Dúvida**Por que o  sistema esta gerando conta bloqueada , sem saldo anterior e ou sem movimento no período?

Sistema esta gerando na ECD contas I050 e I051 que não possuem saldo anterior e movimento no período

Sistema esta gerando na ECF contas J050 e J051 que não possuem saldo anterior e movimento no período  
  
**Ambiente**  
Microsiga Protheus – Contabilidade  – A partir da versão 11.80  
  
**Solução**

1. A gerar a ECD veja como gerar o [I050 e I051](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022515312-MP-SIGACTB-ECD-COMO-GERAR-OS-REGISTROS-I050-E-I051-PLANO-DE-CONTAS-E-PLANO-DE-CONTAS-REFERENCIAL?source=search) corretamente
2. Ao gerar a ECF veja como gerar o [J050 e J051](http://tdn.totvs.com/pages/releaseview.action?pageId=284465420) corretamente
3. Caso a conta esteja bloqueada mais tenha saldo anterior e ou movimento no período , o sistema irá gerar
4. Veja se a conta possui saldo anterior, movimento no período, se algum dia teve movimento e como ela foi zerada , veja como esta a tabela abaixo  
   [CT2,CQ0,CQ1(..)CQ9, CTC,CTF, CV7,CV8, CVX, CVY, CVZ](http://tdn.totvs.com/display/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB)  

   CT2 - Movimento Plano de Contas

   CQ0 e CQ1 Saldos Planos de Contas

   CQ2 e CQ3 Saldos Centro de Custo

   CQ8 e CQ9 Saldos Totais por Entidade

   [Compartilhamento das tabelas](http://tdn.totvs.com/display/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB)
5. Caso esteja gerando ECD com [Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046818313-MP-SIGACTB-ECD-I100-Centro-de-Custo?source=search) e o centro de custo tenha saldo anterior e ou movimento no período a conta será gerada no arquivo
6. Caso esteja gerando ECF com [Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006871231-MP-SIGACTB-ECF-Centro-de-Custo?source=search) e o centro de custo tenha saldo anterior e ou movimento no período a conta será gerada no arquivo
7. Verifique se a situação persiste em base teste realize a  [LIMPEZA TABELA CS3 e CS4](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026508851-MP-SIGACTB-ECD-LIMPEZA-TABELA-CSB?source=search)
8. As tabelas CSA e CSB são alimentadas com base nas tabelas CTC e CTF  
   **[Pacotes de Atualização - Contabilidade +Procedures + dicionário](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777)**  
     
   **Diretamente no servidor  
   Em modo exclusivo:  
   1º Reinicie o serviço.  
   2º Desinstale as procedures existente em seu ambiente.  
   3º Verifique se o sistema desinstalou do configurador.  
   4º Verifique se o sistema [desinstalou do Banco](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019534772-MP-SIGACTB-Saldos-n%C3%A3o-est%C3%A3o-sendo-atualizados-de-forma-online-?source=search) antes de instalar novamente.  
   5º Copie as [procedures atualizadas](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777) na pasta system.  
   6º Instale as procedures .  
   7º Reinicie o serviço.**
9. Realizar o reprocessamento de saldo com Base no primeiro lançamento existente na tabela CT2 até a data de hoje. (Importante que o reprocessamento seja realizado  com a data correta para que a tabela CTC e CTF seja alimentada
10. Emita relatório para verificar se as entidade (Conta , centro de custo) possuem saldo anterior e ou movimento no período  
      
    [- Relatórios com Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018817912-MP-SIGACTB-Relat%C3%B3rios-com-Centro-de-Custo)  
    - [Documentação CTBR400 e CTBR040](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115016115388-MP-SIGACTB-Saldo-anterior-zerado?source=search)  
      
    Saiba mais

[MP - SIGACTB : ECD I051: COD\_CTA\_REF ; Conta não existe no plano de contas referencial informado no registro 0000 (COD\_PLAN\_REF).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048292614-MP-SIGACTB-ECD-I051-COD-CTA-REF-Conta-n%C3%A3o-existe-no-plano-de-contas-referencial-informado-no-registro-0000-COD-PLAN-REF-?source=search)

[MP - SIGACTB : ECD I051 COD\_PLAN\_REF O registro I051 é obrigatório quando existe código do plano de contas referencial informado no](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048293454-MP-SIGACTB-ECD-I051-COD-PLAN-REF-O-registro-I051-%C3%A9-obrigat%C3%B3rio-quando-existe-c%C3%B3digo-do-plano-de-contas-referencial-informado-no-registro-?source=search)
