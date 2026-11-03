---
content_hash: 07bde3dfb47a5dc0b9753f9ff2be8b3e57b836e30e23a9f0e4fd55546c37beee
fetched_at: '2026-06-29T00:06:07.758896+00:00'
page_id: '201737658'
product: rm
source: tdn-rm
title: TTEMO9_DT_Calculo_Salario_Composto_Reprogramacao_Salarial_Proporcionalizar_Dias
type: documentation
url: https://tdn.totvs.com/display/LRM/TTEMO9_DT_Calculo_Salario_Composto_Reprogramacao_Salarial_Proporcionalizar_Dias
version: 2
---

# CÁLCULO SALÁRIO COMPOSTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cálculo do salário composto* |
| **Situação/Requisito:** | Ao realizarmos uma reprogramação salarial, para um professor que teve inicio das atividades no meio do mês, exemplo dia 20, o sistema faz a reprogramação salarial perfeitamente, gerando um valor de 10 dias para o professor, esse valor é levado para o salario composto do mesmo.Porém se o mesmo professor for admitido no mês, exemplo data de admissão dia 20, o sistema TOTVS Folha de Pagamento, está proporcionalizando novamente, pegando o salário já reprogramado de 10 dias, divide por 30 e multiplica por 10 novamente. |
| **Solução/Implementação:** | *Ajustado cálculo do salário composto para que no mês da admissão não seja feita a proporcionalização, considerando apenas a proporcionalização da reprogramação salarial.* |
| **Conversores e Parâmetros:** | *Integração Educacional: Proporcionalizar número de dias* |
| **Chamados relacionados:** | *TTEMO9* |
| **Versões/Release:** | *12.1.8* |
