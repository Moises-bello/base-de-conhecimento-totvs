---
content_hash: 182538038e21ba73bf89689663f6843a450f9f80ec5aec580105c73febbf7c6a
fetched_at: '2026-06-29T00:08:41.357036+00:00'
page_id: '286722599'
product: rm
source: tdn-rm
title: RMCTB00002_Associação Dinâmica de Centro de Custo/Conta Gerencial ao Plano
  Paralelo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286722599
version: 9
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS - Gestão Contábil |
| **Versões:** | 12.1.17 |
| **Ocorrência:** | Associação Dinâmica de Centro de Custo/Conta Gerencial |
| **Ambiente:** | Novo Modelo BackOffice |
| **Passo a passo:** | **Definição do processo**  O objetivo deste processo é evitar diferenças de apuração no mapeamento gerencial com o plano paralelo no PVA (Programa Validador do SPED Contábil), como também diminuir consideravelmente o trabalho de associação de dados gerenciais ao mesmo.  A Associação Dinâmica do Centro de Custo/Conta Gerencial ao Plano Paralelo é o processo responsável por fazer automaticamente a associação dos centros de custos ou contas gerenciais conforme utilização indicada nos Parâmetros do TOTVS Gestão Contábil em: Ambiente / Parâmetros / TOTVS Gestão Contábil / Rotinas Legais / Sped Contábil 1/2:    A associação dinâmica somente será feita às contas contábeis que estiverem associadas às contas paralelas e para os Centros de Custos / Contas Gerenciais cujo campo: Enviar para o Sped esteja devidamente marcado e terem sidos movimentados no período informado.  Na execução deste processo, o sistema primeiramente removerá todas as associações de Centros de Custos / Contas Gerenciais que porventura existirem no plano paralelo informado, para em seguida fazer dinamicamente as novas associações.  **DESENVOLVIMENTO/PROCEDIMENTO**  1 - Primeiramente associe todas as contas contábeis às contas paralelas correspondentes:  Para isto acesse: Cadastro / Plano Paralelo / Anexos / Contas Paralelas. Edite a conta paralela e associe à ela a conta contábil. Repita este passo para todas as contas paralelas.  Depois de associar todas as contas contábeis, execute o processo para fazer a associação dinâmica.  Para isto acesse o Cadastro: Plano Paralelo / Processos / Associação Dinâmica do Centro de Custo/Conta Gerencial ao Plano Paralelo:  2 - Informe a data limite para alteração e execute:  Informe o período para que o sistema identifique os centros de custos / contas gerenciais utilizados nos lançamentos neste período:                                  3 - Após a execução acesse o bloco de notas para verificar os avisos do sistema: |
| **Observações:** | * A associação dinâmica somente será feita às contas contábeis que estiverem associadas às contas paralelas; * A associação dinâmica somente será realizada para os Centros de Custos / Contas Gerenciais cujo campo: Enviar para o Sped esteja devidamente marcado e terem sidos movimentados no período informado, acesse o Menu: Cadastros / Centros de Custos e verifique se este está devidamente marcado; * No final do processo será gerado um LOG com as informações processadas. * Nos Parâmetros do Sistema/Rotinas Legais deve ser devidamente indicado que informação a sua empresa irá considerar para o SPED Contábil, marcando uma das duas opções: ‘O próprio Centro de Custo’ ou ‘Conta Gerencial’. |
