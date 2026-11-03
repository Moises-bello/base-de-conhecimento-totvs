---
content_hash: 04712a3b755f00113bd8a641f3ef7da8cb769a39b875b894dcdf6f6617920262
fetched_at: '2026-06-29T00:08:57.228804+00:00'
page_id: '353284122'
product: rm
source: tdn-rm
title: RMCTB0005_REGISTRO I050
type: documentation
url: https://tdn.totvs.com/display/LRM/RMCTB0005_REGISTRO+I050
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Contábil |
| **Versões:** | 12.1.XX |
| **Ocorrência:** | Erro no Registro I050 |
| **Ambiente:** |  |
| **Passo a passo:** | **Processo:**  Erro apresentado ao validar o arquivo da ECD no PGE (Programa Gerador de Escrituração):  **CONTA DE NÍVEL SUPERIOR DEVERÁ TER A MESMA NATUREZA DA SUB-CONTA**  **Análise/Solução**  A(s) conta(s) analítica(s) indicada(s) no validador deverá(ão) possuir a mesma ‘Natureza da Conta para Emissão do SPED’ da conta sintética correspondente.  Acesse o Plano de Contas Contábeis e verifique o preenchimento do campo Natureza da Conta para Emissão do SPED das Contas analíticas e sintéticas correspondentes.  Veja um exemplo abaixo:   Veja que a conta 1.1.3.6 esta com a classificação igual a 01 (Contas de Ativo), porém a conta 1.1.3.6.001 esta com a classificação igual 02 (Contas de Passivo).  Para o mesmo grupo, a classificação deve ser igual entre as contas, neste caso, o certo seria alterar a classificação de 02 para 01.  Para a alteração acesse o menu Cadastros | Plano de Contas Contábil | Edite a respectiva conta e altere o campo Natureza da Conta para Emissão do SPED | Salvar.  Ou execute o processo [Classificação Automática da Natureza para Emissão do SPED](https://tdn.totvs.com/pages/viewpage.action?pageId=286519602). |
| **Observações:** |  |
