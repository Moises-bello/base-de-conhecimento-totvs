---
content_hash: e6ffde1907d744d240647f9543ea52d4b733eecf3c5b540f6e53f8bb55182086
fetched_at: '2026-06-29T00:11:48.540997+00:00'
page_id: '82477738'
product: rm
source: tdn-rm
title: RMFIS00022_Parametrização para gerar Registros F120 e F130
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=82477738
version: 5
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:** 11.5x |
| **Processo** | **:** | EFD Contribuições |
| **Subprocesso** | **:** | Parametrização para gerar Registros F120 e F130 |
| **Data da publicação** | **:** | 20/08/2013 |

Operações geradoras de créditos com base nos encargos de Depreciação e Amortização e Valor de Aquisição. Para geração desses registros será preciso ter o sistema de **Gestão Patrimonial** implantado. Também para estes Registros, foi criado o conceito de Processo onde devem ser informados os Bens que irão compor os valores dos registros.

Será preciso parametrizar um Processo na Gestão Fiscal, menu **Opções\Parâmetros\Processos\EFD COFINS:**

Grupo **“Registro F120 – Credito Ativo Imobilizado”,**criar um SubGrupo com todos os Bens que serão utilizados na geração dos **Registro F120 ou F130:**

**Registro F120 e F130** – Associar a Tabela de Bens ao Sub- Grupo “Ativo Imobilizado” e Informar:

√  **Método de Apropriação do Crédito**(Depreciação, Amortização ou custo de Aquisição); Caso seja selecionada a Opção “Custo de Aquisição”, deve-se informar o número de parcelas a serem apropriadas.

√  **Grupo do Bem**(de acordo com Tabela do Manual da EFD);

**√  Utilização do Bem**(de acordo com tabela do Manual da EFD).

**Registro F120 e F130** – Na pasta Filtro, informar os bens que geram direito ao crédito do**PIS/COFINS** e aqueles que não geram direito ao crédito de acordo com a Legislação. Os valores de depreciação\amortização\aquisição dos bens que não geram crédito do **PIS\COFINS** irão compor o valor do campo **07 – PARC\_OPER\_NÃO\_BC\_CRED** dos Registros correspondentes.

**Registro F120 e F130** – Para cada Sub\_Grupo, informar ainda:

√  Os Tributos**PIS** e **COFINS**. O Sistema só pode permitir associar os Tributos com Tipo Tributo “**10-PIS\PASEF” ou “11- COFINS**”;

√  O Código da Situação Tributária – CST do Tributo (Campo Livre para digitação, numérico, dois dígitos)

Para maiores informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/_layouts/searchresults.aspx?k=diferencial%20de%20al%C3%ADquota&u=http%3A%2F%2Fwikihelp%2Etotvs%2Ecom%2Ebr%2FWikiHelp)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
