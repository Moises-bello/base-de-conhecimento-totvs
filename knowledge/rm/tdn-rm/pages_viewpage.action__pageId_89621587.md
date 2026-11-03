---
content_hash: 547811377cfd8899a5acab3d2031aec758376c1c8dd8bea6992121c8d321a402
fetched_at: '2026-06-29T00:12:01.545806+00:00'
page_id: '89621587'
product: rm
source: tdn-rm
title: RMFIS00023_Registro F500 - Juros/Multa e Fórmula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=89621587
version: 11
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:** 11.52 |
| **Processo** | **:** | Geração do EFD PIS/COFINS |
| **Subprocesso** | **:** | Registro F500 - Juros/Multa e Fórmula |
| **Data da publicação** | **:** | 22/10/2013 |

**Registro F500 – Base de Cálculo Juro e Multa**

* **É imprescindível ter o sistema TOTVS Gestão Financeira(RM Fluxus) instalado e parametrizado no ambiente de geração.**

Processo semelhante ao existente hoje para geração do F100. Ao selecionar a opção "Juros e Multa" no Campo Base de Cálculo, será gerado um **Registro F500** e filhos separados das demais receitas. O **Registro F500** foi evoluído para suportar a geração dos Juros e Multa, igual ao que é feito para o **F100**.

Neste caso de Juros e Multa o **Registro F525** será gerado com Campo **"03 IND\_REC "** - Indicador da Composição da Receita Recebida no Período igual a **"99- Outros"** e observação "Total de juros e multas recebidos no Período".

Será Gerado somente um Registro F500/F525 com o Total de Juros e Multa de todos os lançamentos do Período.

Cadastro Tipo de Documento Fiscal

Para atender essa demanda é imprescindível que seja criado um Tipo de Documento (fictício) para ser associado ao Processo. Isso é necessário porque o campo é parte da chave primária do cadastro, tornando seu preenchimento obrigatório. Esse Tipo de Documento não será utilizado em nenhum outro processo e não afetará nenhum cálculo do sistema.

No Menu Opções | Parâmetros | Processo | EFD PIS\COFINS – Registro F100\F500 -  Registro F100\F500 habilitado Tipo de Registro F500, no Campo Base de Cálculo informar (Valor dos Juros + Valor da Multa).

Informar o PIS e COFINS com os respectivos CST's.

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F500 | 67,00 | 08 | 0,00 | 67,00 | 0,00 | 0,00 | 08 | 0,00 | 67,00 | 0,00 | 0,00 | Total de juros e multas recebidos no período |
| F525 | 67,00 | 99 | 67,00 | 08 | 08 | Total de juros e multas recebidos no período |

OBSERVAÇÕES:

O processo Cálculo das Contribuições *Dcts* Não Escriturados (Utilitários) irá desconsiderar esse registro. Ou seja, não serão inseridos nos Tributos do Lançamento Financeiro, os tributos PIS e COFINS sobre juros e multas, que serão identificados através da Base de Cálculo: "(Valor dos Juros + Multa)", informado no Processo. Assim, os registros que estiverem a Base de Cálculo igual "(Valor dos Juros + Multa)", serão desconsiderados no processo Cálculo das Contribuições *Dcts* Não Escriturados (Utilitários).   
   
  
 **Registro F500 – Base de Cálculo através de Fórmula**

O Registro F500 foi evoluído para suportar a geração da Base de Cálculo utilizando Fórmula.

**Fórmula do RM Fluxus**

Cadastra no Aplicativo Gestão Financeira (RM Fluxus) uma Fórmula que será utilizada para Calcular a Base de Cálculo do Registro F500 e filhos.   
 Menu Opções | Parâmetros | Processo | EFD PIS e COFINS – Registro F100\F500

Selecionado o Tipo de Registro F500 será possível utilizar no Campo Base de Cálculo "Utiliza Fórmula"

   
Utilizando esta opção ao incluir os Tributos PIS e COFINS, será habilitado um campo para informar "Cod Fórmula" e "Título". Esta Fórmula é criada no aplicativo "Gestão Financeira" (RM Fluxus).

OBSERVAÇÕES:

O processo Cálculo das Contribuições *Dcts* Não Escriturados (Utilitários) irá considerar esse registro. Ou seja, serão inseridos nos Tributos do Lançamento Financeiro, os tributos PIS e COFINS.

Para maiores informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/Fis.EFDLucroPresumido.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
