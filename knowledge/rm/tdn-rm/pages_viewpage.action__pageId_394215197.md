---
content_hash: 497530f4ac862c00b1a3f4db398f6e6f994f03601e3d4a9b200f4635b7dc6434
fetched_at: '2026-06-29T00:09:09.909729+00:00'
page_id: '394215197'
product: rm
source: tdn-rm
title: 3712105 EDUCACIONAL01-6258 DT Fórmulas Visuais de Matrícula validar contexto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=394215197
version: 1
---

# FÓRMULAS VISUAIS DE MATRÍCULA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Alterar situação de matrícula |
| **Situação/Requisito:** | Ao executar o processo de alteração de situação de matrícula, utilizando fórmula visual configurada nos Parâmetros Educacional | Matrícula | Fórmulas visuais, caso a mesma executasse a atividade rmsSaveRecordActivity1 no DataServer EduAlunoData, apresentava mensagem “Contexto inválido OU não foram configurados os parâmetros do Educacional correspondentes ao contexto: Coligada {1}, Filial {-1}, Nível de Ensino {2}.” |
| **Solução/Implementação:** | Otimizado a execução de fórmula visual para gravar dados do aluno, quando utilizado a atividade rmsSaveRecordActivity1 no DataServer EduAlunoData. A execução da fórmula está configurada nos Parâmetros Educacional | Matrícula | Fórmula visual, campo “Após execução da alteração da situação do período letivo”. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
