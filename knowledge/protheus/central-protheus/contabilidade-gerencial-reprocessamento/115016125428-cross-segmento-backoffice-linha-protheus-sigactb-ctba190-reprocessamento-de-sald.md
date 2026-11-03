---
article_id: 115016125428
category: Contabilidade Gerencial - Reprocessamento
content_hash: a1f89fdc4edc25c62c230b0b7fe285eef4241120a3d03099c268e5285d63fe86
fetched_at: '2026-06-28T22:40:41.913222+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA190 - Reprocessamento
  de Saldos: Erro na Chamado do Processo'
type: support-article
updated_at: '2025-02-13T13:07:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115016125428-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA190-Reprocessamento-de-Saldos-Erro-na-Chamado-do-Processo
---

**Ocorrência**Ao executar a rotina de Reprocessamento de Saldos é exibido a mensagem: *ERRO NA CHAMADA DO PROCESSSO*

***![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072849033)***

**Ambiente**  
Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
**Causa**Este tipo de erro **somente** ocorre quando utilizado o pacote de *Stored Procedures* *para a rotina **Reprocessamento de Saldos**. O Protheus exibe essa mensagem quando ocorre alguma não-conformidade na execução da procedure dentro do banco de dados e para uma analise do erro o cliente deve abrir o TopConnect/DbAccess e na aba **Mensagem** verificar a mensagem enviada pelo banco de dados.*  
Basicamente para analisar estes tipos de erros deve verificar os itens abaixo:  
1º) Verifique via Configurador se as *Stored Procedures* estão todas instaladas e com a mesma assinatura para a *Stored Procedures* e rotina ADVPL.  
2º) Desinstalar as *Stored Procedures* e instalar novamente. Baixar e subir o *SERVER* do sistema e tentar processar novamente.  
3º) Analisar o erro gerado no *TopConnect/DbAccess*(Caso não tenha conhecimentos em banco de dados recomendo a solicitação de um DBA Totvs).  
4º) Erro pode estar sendo apresentado devido tamanho de campos ou grupo de perguntas CTB190,CTB211,CTB215(...)  estarem incorretos

**Requisitos**

* Acesse aqui as ultimas expedições **Pacote Acumulado Contábil +procedure nela existente :**
* **[Pacotes LIB](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/search/searchAll)**
* **[Pacotes DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/search/searchAll)**
* **[Binário AppServer](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/)**
* **[Binário SmartClient](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFSC/)**
* [Pacotes de Atualização - Contabilidade](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777)

**Solução**

1.Realize as desinstalação e a [Instalação das Procedure](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011410951-MP-SIGACTB-SIGAATF-Instala%C3%A7%C3%A3o-de-Procedure-?source=search)2. Violação de Chave única da tabela :Verificar procedimento descrito no link: [Erro ao atualizar os saldos (Unique constraint)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000737728-MP-SIGACTB-Erro-ao-atualizar-os-saldos-Unique-constraint-)

Obs: podendo ser apresentado em Tela ou no Trace

3. Estouro de Campo  
Em caso de Estouro de Campo, deve-se verificar qual é o campo e avaliar a alteração da estrutura de todas as tabelas de saldos para o maior tamanho possível ,sugerimos realizar a  [ALTERAÇÃO DO TAMANHO DAS ENTIDADES CONTÁBEIS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015543251-MP-SIGACTB-ALTERA%C3%87%C3%83O-DO-TAMANHO-DAS-ENTIDADES-CONT%C3%81BEIS?source=search) , [Tamanho do campo código das entidades contábeis Adicionais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024401031-MP-SIGACTB-Alterar-o-tamanho-do-campo-c%C3%B3digo-das-entidades-cont%C3%A1beis-adicionais?source=search) e [Tamanho do campo código das entidades contábeis Adicionais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024401031-MP-SIGACTB-Alterar-o-tamanho-do-campo-c%C3%B3digo-das-entidades-cont%C3%A1beis-adicionais?source=search) estão corretos.

* Veja se o [compartilhamento de tabelas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018270032-MP-SIGACTB-Como-realizar-compartilhamento-de-tabelas-no-Contabilidade-Gerencial-SIGACTB-?source=search)saldo e movimento estão corretas (CT2,CTC,CQ0...CQ9)

4. Veja se o parametro [MV\_ATUSAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019534772-MP-SIGACTB-Saldos-n%C3%A3o-est%C3%A3o-sendo-atualizados-de-forma-online-?source=search) está configurado corretamente

5. Realize o  [reprocessamento de saldos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007452371-MP-SIGACTB-CTBA-190-Como-realizar-o-reprocessamento-de-saldos-no-SIGACTB-?source=search) 

Saiba mais:

[MP - SIGACTB - CTBA220 ERRO NA CHAMADA DO PROCESSO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023000092-MP-SIGACTB-CTBA220-ERRO-NA-CHAMADA-DO-PROCESSO?source=search)

[MP - SIGACTB - FALHA NA CHAMADA DO PROCESSO CTBA185\_06](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006993712-MP-SIGACTB-FALHA-NA-CHAMADA-DO-PROCESSO-CTBA185-06?source=search)
