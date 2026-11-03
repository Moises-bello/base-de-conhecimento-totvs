---
article_id: 8746011684631
category: 'Fiscal Arquivos Magnéticos - Complementos de Notas Fiscais '
content_hash: d74c5716e87204a5da08bc1ccf39cb012e8c0caecd864d0f9c1d09f70d520b16
fetched_at: '2026-06-28T22:41:59.477645+00:00'
product: protheus
section_id: 7707613209239
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Complementos
  MATA926 Help: Um ou alguns campos obrigatórios não foram preenchidos'
type: support-article
updated_at: '2025-05-27T14:06:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8746011684631-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Complementos-MATA926-Help-Um-ou-alguns-campos-obrigat%C3%B3rios-n%C3%A3o-foram-preenchidos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:02:00 min **Dúvida**Como salvar com sucesso os **Complementos de Nota Fiscal** na **Rotina MATA926** quando ocorre mensagem de *Help*: **Um ou alguns campos obrigatórios não foram preenchidos**?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

O alerta (A926DOCOBR), é referente à falta de **"Informações Complementares e Documentos Fiscais "** referenciados que se encontram dentro do caminho:   
**Livros Fiscais / Rotina NF Saída Manual / Selecionar nota Fiscal / Ações Relacionadas / Complementos / Informação Complementares e Documentos Fiscais**A mensagem ocorre porque tem algum campo que não foi preenchido. O sistema não informa qual (is) campos devem ser preenchidos, pois todos os campos apresentados nos **Complementos** que está habilitado para preenchimento **são de obrigatoriedade do Fisco**, para evitar erros na **transmissão de NF-e** e/ou na **geração das obrigações fiscais**.  
  
O fiscal da empresa precisa avaliar quais campos devem ser preenchidos, e caso algum campo não necessite de preenchimento, realizar o processo de desobrigação dos mesmos. Para conseguir salvar o complemento todos os campos devem ser preenchidos, caso algum campo não necessite de preenchimento, seguir o procedimento abaixo:  
  
1. **Acesse a APSDU**. - > Filtra SX3 (Dicionário de dados) deste ambiente.  
2. **Realize o Filtro dos campos do complemento.**  
3. **Faça um backup da tabela SX3**.  
3. **Apague o conteúdo do campo X3\_RESERV.**  
4. **Saia da APSDU**.  
5. **Acesse o Configurador do M. Protheus (SIGACFG)**.  
6. **Abra a Tabela\* correspondente** -> Filtrar os campos desejados  
7. **Desabilite a Obrigatoriedades dos campos**. 

Ao clicar em **Salvar**, se e o sistema retornar novamente com a tela do *Help,* verifique se mais algum complemento precisa ser preenchido. Caso o não preenchimento, o sistema irá retornar novamente o aviso que existem campos a preencher.

![imagem_kcs1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/8745869599767/imagem_kcs1.PNG)  
  
Também verifique se o sistema habilitou mais algum complemento em **"Informações Complementares"**. Pois, se a mensagem ocorrer novamente, algum campo não deve ter sido habilitado e ou outros campos estão sendo considerados.  
  
![imagem_kcs2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/8745876816151/imagem_kcs2.PNG)

\***Água canalizada = Tabela CD4**  
**Armas de Fogo = Tabela CD8**  
**Combustível = Tabela CD6**  
**Comunicação e telecomunicação = Tabela SFX**  
**Energia elétrica = Tabela SFU**  
**Gás canalizado = Tabela CD3**  
**Importação = Tabela CD5**  
**Medicamentos = Tabela CD7**  
**Veículos automotores = Tabela CD9**   
**Exportação = Tabela CDL**
