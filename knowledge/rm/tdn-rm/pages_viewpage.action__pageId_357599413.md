---
content_hash: d5cde155d6dc7ef01951ab2ded127e24d753787972069eae7db0ad5fa05232d4
fetched_at: '2026-06-29T00:08:57.915957+00:00'
page_id: '357599413'
product: rm
source: tdn-rm
title: RMCTB00003_Como gerar ECD para SCP - Controle de Sociedades em Conta de Participação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=357599413
version: 4
---

# 

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Contábil |
| **Versões:** | 12.1.XX |
| **Ocorrência:** | ECD - Geração do arquivo para SCP |
| **Ambiente:** |  |
| **Passo a passo:** | **Definição do Processo:**  A partir do ano base de 2015, a forma de Escrituração (Escrituração SCP Mantida pelo Sócio Ostensivo) deixa de existir, ou seja, não poderá mais enviar as informações da SCP usando a opção conforme print:  abaixo:    **Desenvolvimento/Procedimento**  Abaixo, será demonstrado de como deverá ser gerado o arquivo para as empresas SCPs:    A forma de Escrituração a ser usada será a mesma escrituração usada para a Sócio Ostensiva.  Por exemplo: Forma de Escrituração Livro Diário (Completo, sem escrituração auxiliar)  Esta Escrituração será usada  tanto para o Sócio Ostensivo, quanto para a SCP.  Na geração do arquivo o Indicador do tipo de ECD deverá ser ECD da SCP e sua filial deve ser informada:    Não se esqueça de informar o histórico padrão do encerramento das contas de resultado da filial correspondente à SCP, realize o mesmo processo com a sócio ostensivo: |
| **Observações:** | Lembrando que a forma de Escrituração será a mesma tanto para o sócio ostensivo quanto para SCP, o que definirá cada uma será somente o Tipo de Indicador ao gerar o arquivo. |
