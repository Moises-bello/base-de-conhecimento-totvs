---
content_hash: 87f9fdd2dfbe17d01923702281a54e9fd1e563241464a531f1fb3a0d25bf4792
fetched_at: '2026-06-29T00:09:20.189311+00:00'
page_id: '422545677'
product: rm
source: tdn-rm
title: EFD Contribuições (Lucro Presumido)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545677
version: 6
---

Os registros referentes à escrituração do PIS e da COFINS das pessoas jurídicas sujeitas ao regime de tributação com base no Lucro Presumido, aplicável aos fatos geradores a ocorrer a partir de 01 de julho de 2012, serão disponibilizados pelo Programa Validador e Assinador (PVA) da EFD Contribuições a partir da versão 2.01.

A empresa tributada pelo Lucro Presumido e que também se enquadre na incidência da contribuição previdência sobre a receita bruta, deve apresentar a EFD Contribuições a partir de março ou abril de 2012 apenas com as informações da contribuição previdenciária (Bloco P). As informações sobre a apuração do PIS e da COFINS devem ser informadas a partir de julho de 2012.

As empresas estão dispensadas de entregar a EFD Contribuições nos meses que não auferiu receitas sujeitas ao pagamento das contribuições. No mês de dezembro, entretanto, deve ser entregue a EFD informando os meses do ano-calendário em que não auferiu receitas no Registro 0120. Este registro não será gerado pelo RM.

Para o regime do Lucro Presumido devem ser informadas apenas as operações representativas de receita nos blocos a seguir:

* F500 e filhos para o Regime de Caixa - Escrituração Consolidada. As informações serão carregadas do TOTVS Gestão Financeira.

***Observação:*** Para a correta seleção dos lançamentos financeiros foi criado um processo (semelhante ao do F100) no qual serão informados os tipos de documento utilizados no TOTVS Gestão Financeira que irão gerar informações  de Contribuição/Crédito.

Este processo pode ser acessado no TOTVS Gestão Fiscal no menu Opções | Parâmetros | Processos – EFD PIS/COFINS – Registro F100/F500 - Tipos de Documentos Considerados. Ao criar o processo deverão ser informados os tipos de documento que irão gerar as informações. Para cada [Tipo de Documento](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388695) deverão ser incluídos os Tributos PIS e COFINS com os respectivos CST.

Este processo deverá ser executado sempre antes de ser disparada a geração da rotina para que a informação dos tributos seja inserida nos lançamentos financeiros. O processo poderá ser executado sempre que for feita a inclusão de novos lançamentos ou os mesmos sofrerem alteração em seus valores.  
O processo é disparado através do menu Utilitários | Cálculo das Contribuições Docs não escriturados.

Blocos A, B, C, D e F para o Regime de Competência - Escrituração detalhada. A origem das informações e parametrizações são as mesmas utilizadas na geração para o lucro real.

---
