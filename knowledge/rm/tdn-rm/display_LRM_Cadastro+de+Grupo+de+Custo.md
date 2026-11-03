---
content_hash: b7e843895e9bb641f362c2258f5ea36fca39c141a7476c9cfa0249cceab9eda2
fetched_at: '2026-06-29T00:09:16.160542+00:00'
page_id: '421385471'
product: rm
source: tdn-rm
title: Cadastro de Grupo de Custo
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastro+de+Grupo+de+Custo
version: 1
---

**Cadastro de Grupo de Custo**   
Nesta opção cadastra-se a tabela de grupos de custo.   
Através do cadastro é possível controlar:  
   
**Pasta Identificação**  
   
Nesta pasta, serão informados os dados que identificarão o grupo de custo cadastrado.  
   
**Código**  
Informe o código para o grupo de custo. Não é permitida a inclusão de códigos repetidos, portanto, um código somente refere-se a um determinado grupo de custo. Este campo é alfanumérico.  
**Descrição**  
Informe a descrição para o grupo de custo.  
**Condição de Pagamento**  
Informe a condição de pagamento para o grupo de custo, que será considerada no cronograma de desembolso, se não for informada a condição de pagamento no cadastro do insumo. Se a condição de pagamento não estiver informada no cadastro do insumo e nem no cadastro de grupo de custo, será considerada a condição de pagamento definida no menu Opções | Parâmetros | RM Solum | Projetos, pasta Diversos.  
**BDI**  
Taxa de BDI que será aplicada sobre os insumos pertencentes a este grupo de custo. O preço improdutivo do insumo não sofre incidência de leis sociais.  
Este campo não poderá ser nulo ou igual a zero.  
**Exemplo**  
Se um dos insumos pertencentes a esse grupo tem valor unitário 0,47 e aplicamos um bdi de 2,00 sobre o seu grupo de custo, esse insumo passa a custar 0,94. Se houver incidência de leis sociais, primeiro será aplicada a taxa de bdi e depois a taxa de leis sociais.  
**Leis Sociais**  
Marque esta opção caso os insumos deste grupo de custo recebam incidência de leis sociais. Por exemplo, para o grupo de custo "mão-de-obra". Podendo escolher se irá incidir sobre o valor a "lei social 1" ou a "lei social 2", que são parametrizadas no sistema através do menu Opções | Parâmetros | RM Solum | Projetos, pasta Cálculo, subpasta Leis - Outros.  
**Grupo DNIT**  
Marque o grupo DNIT que os insumos deste grupo de custo irão pertencer, Equipamentos (A), Mão de Obra (B), Material (C), Atividades Auxiliares (D), Tempo Fixo (E) e Momento de transporte (F).  
Caso sejam inseridos em composições por produção, é necessário saber se o insumo é do grupo Equipamentos (A) ou Mão-de-obra (B) para habilitar a pasta de custo horário no cadastro do insumo.  
**Equalizável**  
Habilitada esta opção, permitirá dimensionar, a partir dos Insumos associado, a necessidade do recurso, período a período, possibilitando um uso mais linear dos Insumos dentro de cada período do cronograma.  
**Percentual Sobre**  
Pode-se determinar que os insumos pertencentes a um grupo de custo terão seu cálculo baseado num percentual de outro grupo de custo (DNIT ou Custo Unitário). Isso será possível para insumos que tenham a unidade %.  
Quando um recurso de uma composição por produção tiver unidade %, seu valor dentro desta composição será calculado sobre os valores dos insumos pertencentes aos grupos DNIT selecionados no cadastro do seu grupo de custo.  
Quando um recurso de uma composição por custo unitário tiver unidade %, seu valor dentro desta composição será calculado sobre os valores dos insumos pertencentes aos grupos de custo unitário selecionados no cadastro do seu grupo de custo.  
Isso significa que os recursos que têm unidade %, terão seus preços modificados a cada composição.  
**Observações**  
Normalmente, o insumo do grupo ferramenta possui unidade % e seu cálculo é baseado no valor do grupo de custo mão-de-obra. Para que isso seja possível, no cadastro do grupo de custo ferramenta, deve-se informar, no campo "Percentual sobre", o grupo de custo unitário mão-de-obra e no grupo de custo DNIT o grupo A. Isso porque o insumo pode estar inserido numa composição por preço unitário ou composição por produção.  
Se nenhum grupo de custo for selecionado no campo Percentual Sobre, Grupos DNIT, o insumo do tipo percentual inserido numa composição por produção ficará com o valor zero. O mesmo ocorrerá com um insumo do tipo percentual inserido numa composição de preço unitário, se nenhum grupo de custo for selecionado no campo Percentual Sobre, Grupos de Custo Unitário.  
**Exemplos**  
No cadastro de uma composição por custo unitário, o valor do recurso ferramenta será 5% da soma dos preços parciais dos recursos que pertencem ao grupo de custo unitário de mão-de-obra (å Preço Parcial dos recursos de mão-de-obra x 0,05). No cadastro de uma composição por produção, o valor do recurso ferramenta será 5% da soma dos preços parciais dos recursos que pertencem ao grupo B (Mão-de-obra), (å Grupo B x 0,05).  
**Pasta Defaults**  
Esta pasta possibilita a atribuição de valores padrões de grupo de custo unitário, unidade e jornada de trabalho para a faixa de insumos determinada pelos campos "código inicial" e "código final", do grupo de custo em questão. Isso facilita o cadastro de insumos, pois preenche automaticamente os campos "grupo de custo", "unidade" e "jornada de trabalho". Caso desista de utilizar os defaults, basta deixar em branco os campos "código inicial" e "código final".   
**Observações**  
O código inicial e final da faixa de insumos do grupo deverá obedecer a máscara de insumos definida no menu Opções | Parâmetros | RM Solum | Projetos | Pasta Exibição.  
Se a máscara de insumos for alterada ou removida nos parâmetros do projeto, o código inicial e final da faixa de insumos do grupo será apagado.  
**Jornada de Trabalho**  
Informe a jornada de trabalho para o grupo de custo, que será considerada na alocação de recursos. Se a jornada de trabalho não estiver informada no cadastro do insumo e nem no grupo de custo, será considerada a jornada de trabalho definida no menu Opções | Parâmetros | RM Solum | Projetos, pasta Diversos.  
**Prazo de Ressuprimeto**  
Informe a quantidade de dias do prazo de ressuprimento.  
O valor informado neste campo representa a quantidade em dias que o insumo deve chegar para que a tarefa seja entregue na data estipulada.  
**Pasta Campos Complementares**  
São visualizados os campos complementares cadastrados no menu Cadastros | Campos Complementares | Grupo de Custo. Nessa janela os dados devem ser informados. Caso tenha sido definida uma validação do campo complementar com base numa tabela dinâmica, o mesmo será validado nesse momento. Os campos complementares podem ser do tipo Data, Inteiro, Real ou Alfanumérico.
