---
content_hash: d4e86b0de5f22ce36555c914bbbc332c89843e5e1e817492c239012593553771
fetched_at: '2026-06-29T00:06:00.526577+00:00'
page_id: '196809953'
product: rm
source: tdn-rm
title: TSW121_DT_Tolerância_Conforme_CLT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=196809953
version: 5
---

# TOLERÂNCIA DE ACORDO COM O ARTIGO 58

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | **RM** |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | **TOTVS Automação de ponto** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Tolerância* | *Tolerância conforme a CLT (Artigo 58)* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Horário planejado** | *Leitura do horário planejado do funcionário aplicando as tolerâncias* | |
| **Cadastros Iniciais:** | *Acessar o contexto do TOTVS Automação de ponto e na aba "Cadastros", acessar a opção "Limite de tolerância".* |
| **Parâmetro(s):** | *Considera todas as horas para aplicar o limite de tolerância* |
| **Chamados relacionados** | **TSW121** |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas utilizadas:** | *ALIMITETOLERANCIA* |
| **Versões/Release:** | *12.1.7* |

## Descrição

Ao marcar o parâmetro "Considera todas as horas para aplicar o limite de tolerância" (Localizado no cadastro de Limite de tolerância) o sistema vai considerar todas as horas de extras e/ou atrasos para aplicar o limite de tolerância independente do valor da tolerância informada nas batidas do horário.

Exemplo:

Horário planejado: [08:00 12:00] [14:00 18:00]

Horário executado: [07:55 12:00] [14:00 19:00]

Tolerância por batida: 00:05 min.

Limite de tolerância por número de horas: 00:10 min.

Com o parâmetro marcado será gerado: 01:05 hora(s) extra(s)

Com o parâmetro desmarcado será gerado: 01:00 hora(s) extra(s)

## Procedimento para Utilização

1.No contexto do TOTVS Automação de Ponto, acesse Cadastros/Limite de Tolerância.

  2.  Acesse o registro desejado e selecione a opção "Considera todas as horas para aplicar o limite de tolerância".

  3. Certifique que o registro onde o parâmetro foi marcado está vinculado ao horário do funcionário. Essa conferência é realizada através do menu Cadastros / Horários por intervalo, em seguida, acesse a edição do horário e em anexos clique na opção "Limite de tolerância".

  4. Ao processar o recálculo será considerada a tolerância de acordo com os parâmetros acima.
