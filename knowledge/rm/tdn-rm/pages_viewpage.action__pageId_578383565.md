---
content_hash: 226fd611960afbecab3f9522dfaa903d662573a041df96d61f6891079409f89d
fetched_at: '2026-06-29T00:10:53.314762+00:00'
page_id: '578383565'
product: rm
source: tdn-rm
title: Leiaute Versão S-1.0
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=578383565
version: 88
---

false

**A partir das Versões:**

* 12.1.29.284
* 12.1.31.199
* 12.1.32.136
* e Superiores.
falseImportante!

Para o início da utilização dos eventos de SST é **IMPORTANTE** executar a rotina [Limpar Fila de Eventos](https://tdn.totvs.com/display/public/LRM/Limpar+Fila+de+Eventos).

# Objetivo:

---

Apresentar as mudanças no sistema para o leiaute do eSocial Versão S-1.0.

---

11ParametrizaçãoParametrização

Foi liberado em RH | Folha de Pagamento | Configurações | Parametrizador | eSocial | Configurações Gerais | Configurações Gerais 1/6 a versão do leiaute:

* **S-1.0**: Selecionando essa versão será disponibilizado os eventos do novo leiaute S-1.0 conforme publicação no portal do eSocial.

falseImportante!

Antes de alterar para o leiaute S-1.0, é necessário realizar o envio do evento S-1299 - Fechamento dos Eventos Períodicos e que não tenha eventos com status diferente de "Aceito RET" na fila de  eventos.

Após a liberação da versão será necessário executar os script's de adequação das tabelas e campos do sistema através do sistema **RM.Atualizador.exe.**

2Eventos excluídosEventos excluídos

Foram retirados de todos os processos e gatilhos (inclusão, edição e exclusão) os seguintes eventos:

* [S-1040 - Tabela de Funções/Cargos em Comissão](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=452718774)









3Eventos alteradosEventos alterados

Acesse o link abaixo para ver as alterações realizadas em cada evento:

# Tabelas/Eventos Iniciais

* [S-1000 - Informações do Empregador/Contribuinte/Órgão Público](https://tdn.totvs.com/pages/viewpage.action?pageId=585318935)
* [S-1005 - Tabela de Estabelecimentos, Obras ou Unidades de Órgãos Públicos](https://tdn.totvs.com/pages/viewpage.action?pageId=585316051)
* [S-1010 - Tabela de Rubricas](https://tdn.totvs.com/pages/viewpage.action?pageId=605863561)
* [S-1020 - Tabela de Lotações Tributárias](https://tdn.totvs.com/pages/viewpage.action?pageId=587630771)
* [S-1070 - Tabela de Processos Administrativos/Judiciais](https://tdn.totvs.com/pages/viewpage.action?pageId=579131357)

# Eventos Periódicos

* [S-1200 - Remuneração de trabalhador vinculado ao Regime Geral de Previdência Social](https://tdn.totvs.com/pages/viewpage.action?pageId=601696062)
* [S-1210 - Pagamentos de Rendimentos do Trabalho](https://tdn.totvs.com/pages/viewpage.action?pageId=606843193)
* [S-1260 - Comercialização da Produção Rural Pessoa Física](https://tdn.totvs.com/pages/viewpage.action?pageId=589507516)
* [S-1270 - Contratação de Trabalhadores Avulsos Não Portuários](https://tdn.totvs.com/pages/viewpage.action?pageId=588689492)
* [S-1280 - Desoneração da Folha e/ou Simples Concomitante (Inf. Comp. Eventos Periódicos)](https://tdn.totvs.com/pages/viewpage.action?pageId=592291764)
* [S-1298 - Reabertura dos Eventos Periódicos](https://tdn.totvs.com/pages/viewpage.action?pageId=592079156)
* [S-1299 - Fechamento dos Eventos Periódicos](https://tdn.totvs.com/pages/viewpage.action?pageId=588687430)

# Exclusão de eventos

* [S-3000 - Exclusão de Eventos](https://tdn.totvs.com/pages/viewpage.action?pageId=586692687)

# Eventos Não Periódicos

* [S-2190 - Admissão de Trabalhador – Registro Preliminar](https://tdn.totvs.com/pages/viewpage.action?pageId=593253092)
* [S-2200 - Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador](https://tdn.totvs.com/pages/viewpage.action?pageId=599378929)
* [S-2205 - Alteração de Dados Cadastrais do Trabalhador](https://tdn.totvs.com/pages/viewpage.action?pageId=594163257)
* [S-2206 - Alteração de Contrato de Trabalho](https://tdn.totvs.com/pages/viewpage.action?pageId=604509965)
* [S-2230 - Afastamento Temporário](https://tdn.totvs.com/pages/viewpage.action?pageId=589523348)
* [S-2298 - Reintegração](https://tdn.totvs.com/pages/viewpage.action?pageId=588691900)
* [S-2299 - Desligamento](https://tdn.totvs.com/pages/viewpage.action?pageId=593253349)
* [S-2300 - Trabalhador Sem Vínculo de Emprego/Estatutário - Início](https://tdn.totvs.com/pages/viewpage.action?pageId=593440097)
* [S-2306 - Trabalhador Sem Vínculo de Emprego/Estatutário - Alteração Contratual](https://tdn.totvs.com/pages/viewpage.action?pageId=599369008)
* [S-2399 - Trabalhador Sem Vínculo de Emprego/Estatutário - Término](https://tdn.totvs.com/pages/viewpage.action?pageId=599877415)

# Eventos SST

* [S-2210 - Comunicação de Acidente de Trabalho](https://tdn.totvs.com/pages/viewpage.action?pageId=594179630)
* [S-2220 - Monitoramento da Saúde do Trabalhador](https://tdn.totvs.com/pages/viewpage.action?pageId=599032982)
* [S-2240 - Condições Ambientais do Trabalho - Agentes Nocivos](https://tdn.totvs.com/pages/viewpage.action?pageId=611308887)
