---
article_id: 10959455509527
category: Comércio Exterior - Easy Import Control - Siscomex
content_hash: 700fb978e2ecdd4ce044bc149cd0cb1a5e978733e3d946c18afefde1c25c9492
fetched_at: '2026-06-28T22:39:45.280345+00:00'
product: protheus
section_id: 1500001538441
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Form. LPCO X Ncm
type: support-article
updated_at: '2022-12-15T17:26:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10959455509527-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Form-LPCO-X-Ncm
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Vinculação do Form.LPCO X N.c.m?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control*- a partir da versão 12.1.27  
  
**Solução**São objetivos do Cadastro de vinculação do Formulário LPCO x N.c.m

* Padronizar a informação prestada.
* Organizar os formulários solicitados para cada órgão anuente.
* Organizar as definições de quais formulários são necessários para solicitar a licença, a permissão, o certificado ou outro para produtos associados à determinadas N.c.m.

**Exemplo**Permite a inclusão de vinculação entre Formulário **LPCO** x **N.c.m.**Restrições:

           - Em cada linha de detalhe, deve ter definido a obrigatoriedade da informação (Campo "**Obrigatório?**").

1. Preencha os campos desejados e confirme a alteração.
2. Acessar o Menu **Atualizações\Portal Unico\Form.LPCO x N.c.m**
3. Clicar no botão "+Incluir"
4. No campo "**Formul.LPCO**" (Dados do formulário), pressionar **F3** e via consulta, selecionar um código válido ( que exista nos detalhes do cadastro de órgão anuentes para o órgão informado )
5. No campo "**N.c.m**" (Dados do formulário) , pressionar **F3** e via consulta, selecionar um código válido ( que exista no cadastro de N.c.m ) e não possua vinculação com o formulário informado.
6. No campo "**Obrigatório**" (Dados do formulário), defina um valor entre  "**1-Sim**" e **"2-Não**"
7. Para adicionar itens vinculados ao formulário e n.c.m, posicione na linha em branco dos detalhes e informe os dados.
8. Para excluir itens, apenas posicione sobre o item desejado e pressione a tecla **DELETE** do teclado.
9. No campo "**Cód.Produto**" (Detalhes do formulário) informar um código válido ( que exista no cadastro de produtos ) e que possua n.c.m igual a da n.c.m vinculada ao formulário atual.
10. No campo "**Obrigatório**" (Detalhes do formulário), defina um valor entre  "**1-Sim**" e "**2-Não**".

**Obs:** o valor default deste campo é carregado conforme o valor definido nos dados do formulário (capa).

1. Para gravar os dados informados, clicar no botão "**Confirmar**"
2. Clicar no botão "**X**" no canto superior direito para encerrar a sub-rotina
3. Clicar no botão "**X**" no canto superior direito para encerrar a rotina

**Exemplo do procedimento**

**Saiba mais**  
[Formulário LPCO x N.c.m](https://tdn.totvs.com/display/PROT/Form.LPCO+X+N.c.m+-+EICLP400)
